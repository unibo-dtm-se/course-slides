import argparse
import re
import sys
from exam import *
from z3 import Int, Solver, sat, Or, And


VERBOSE = True
QUESTION_INDEX_PATTERN = re.compile(r"Q?(\d+)(?:-Q?(\d+))?", re.IGNORECASE)


def log(*args):
    if VERBOSE:
        print("i:", *args, file=sys.stderr)


def create_arg_parser():
    parser = argparse.ArgumentParser(description='Test Generator')
    parser.add_argument("--questions-file", "-q", type=str, help='Path to questions .csv file', default=DEFAULT_QUESTIONS_FILE)
    parser.add_argument("--total-weight", "-w", type=int, help='Total weight of the test', default=9)
    parser.add_argument("--categories", "-c", type=str, nargs='+', help='Categories to include in the test', action='append')
    parser.add_argument("--completely-different", "-d", action='store_true', help='Generate completely different tests (no repeated questions)')
    parser.add_argument(
        "--different-categories",
        action=argparse.BooleanOptionalAction,
        default=True,
        help='Select at most one question from each category (enabled by default)',
    )
    parser.add_argument(
        "--min-questions", "--minimum-questions", "-n",
        type=int,
        help='Minimum number of questions (defaults to the number of target categories)',
    )
    parser.add_argument("--max-grade", "-g", type=int, help='Maximum grade for the test', default=27)
    parser.add_argument("--verbose", "-v", action='store_true', help='Verbose mode')
    return parser


def parse_args(args = sys.argv[1:]):
    parser = create_arg_parser()
    return parser.parse_args(args)


def parse_question_commands(command: str, question_count: int):
    """Parse commands such as ``no Q1 Q3-Q5 keep Q2``."""
    tokens = command.split()
    if not tokens:
        return set(), set()

    indexes = {"no": set(), "keep": set()}
    current_command = None
    command_has_indexes = False
    for token in tokens:
        normalized_token = token.lower()
        if normalized_token in indexes:
            if current_command is not None and not command_has_indexes:
                raise ValueError(f"'{current_command}' must be followed by at least one question index")
            current_command = normalized_token
            command_has_indexes = False
            continue
        if current_command is None:
            raise ValueError("Expected 'no' or 'keep' before the question indexes")

        match = QUESTION_INDEX_PATTERN.fullmatch(token)
        if match is None:
            raise ValueError(f"Invalid question index or range: {token}")
        start = int(match.group(1))
        end = int(match.group(2) or start)
        if start < 1 or end < 1 or start > question_count or end > question_count:
            raise ValueError(f"Question indexes must be between Q1 and Q{question_count}")
        if end < start:
            raise ValueError(f"Question range must be ascending: {token}")
        indexes[current_command].update(range(start, end + 1))
        command_has_indexes = True

    if not command_has_indexes:
        raise ValueError(f"'{current_command}' must be followed by at least one question index")
    overlap = indexes["no"] & indexes["keep"]
    if overlap:
        labels = " ".join(f"Q{index}" for index in sorted(overlap))
        raise ValueError(f"Questions cannot be both replaced and kept: {labels}")
    return indexes["no"], indexes["keep"]


class TestGenerator:
    def __init__(self, db: QuestionsStore, total_weight: int, target_categories: set[Category],
                 completely_different: bool = False, different_categories: bool = True,
                 min_questions: int | None = None):
        self.__db = db
        self.__total_weight = int(total_weight)
        self.__target_categories = {self.__db.category(category) for category in target_categories}
        self.__different_categories = different_categories
        self.__min_questions = len(self.__target_categories) if min_questions is None else int(min_questions)
        if self.__min_questions < 0:
            raise ValueError("Minimum number of questions cannot be negative")
        for category in self.__target_categories:
            assert self.__db.category_size(category) > 0, f"Category {category} is empty"
            assert self.__db.category_weight(category) > 0, f"Category {category} has no weight"
        self.__problem, self.__variables = self.__configure_problem()
        self.__completely_different = completely_different

    def __configure_problem(self):
        solver = Solver()
        variables = dict()
        for category in self.__db.categories:
            variables_in_category = dict()
            for question in self.__db.questions_in_category(category): 
                variable = Int(question.id)
                solver.add(variable >= 0, variable <= 1)
                variables_in_category[question.id] = variable
            if category in self.__target_categories:
                solver.add(sum(variables_in_category.values()) >= 1)
                log(" + ".join(variables_in_category.keys()), ">= 1")
            if self.__different_categories:
                solver.add(sum(variables_in_category.values()) <= 1)
                log(" + ".join(variables_in_category.keys()), "<= 1")
            variables.update(variables_in_category)
        id_to_variables = variables
        solver.add(sum(id_to_variables.values()) >= self.__min_questions)
        log(" + ".join(id_to_variables.keys()), ">=", self.__min_questions, "questions")
        variables = {k: (v, self.__db.question(k).weight) for k, v in variables.items()}
        solver.add(sum(w * v for v, w in variables.values()) == self.__total_weight)
        log(" + ".join(f'{q} * {w}' for q, (v, w) in variables.items()), "==", self.__total_weight)
        return solver, id_to_variables

    @property
    def solutions(self):
        while (solution := self.next_solution()) is not None:
            yield solution

    def next_solution(self, required_question_ids=(), excluded_question_ids=()):
        required_question_ids = set(required_question_ids)
        excluded_question_ids = set(excluded_question_ids)
        overlap = required_question_ids & excluded_question_ids
        if overlap:
            raise ValueError(f"Questions cannot be both required and excluded: {sorted(overlap)}")
        unknown_ids = (required_question_ids | excluded_question_ids) - self.__variables.keys()
        if unknown_ids:
            raise KeyError(f"Unknown question ids: {sorted(unknown_ids)}")

        self.__problem.push()
        try:
            for question_id in required_question_ids:
                self.__problem.add(self.__variables[question_id] == 1)
            for question_id in excluded_question_ids:
                self.__problem.add(self.__variables[question_id] == 0)
            if self.__compute_next_solution() != sat:
                return None
            solution = self.__solution_to_questions()
        finally:
            self.__problem.pop()

        self.__exclude_solution(solution)
        return solution

    def __exclude_solution(self, solution):
        variables = self.__variables
        current_solution = {variables[q.id]: 1 for q in solution.questions}
        constraint = And if self.__completely_different else Or
        constraint_name = ' and ' if self.__completely_different else ' or '
        self.__problem.add(constraint([x != y for x, y in current_solution.items()]))
        log("add constraint:", constraint_name.join([f'{q.id} != 1' for q in solution.questions]))

    def __compute_next_solution(self):
        log("computing next solution...")
        return self.__problem.check()

    def __solution_to_questions(self):
        questions = []
        model = self.__problem.model()
        solution = {q: model[v].as_long() for q, v in self.__variables.items()}
        for question_id, value in solution.items():
            if value != 0:
                questions.append(self.__db.question(question_id))
        return QuestionsStore(questions)
