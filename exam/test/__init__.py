import argparse
import sys
from exam import *
from z3 import Int, Solver, sat, Or, And


VERBOSE = True


def log(*args):
    if VERBOSE:
        print("i:", *args, file=sys.stderr)


def create_arg_parser():
    parser = argparse.ArgumentParser(description='Test Generator')
    parser.add_argument("--questions-file", "-q", type=str, help='Path to questions .csv file', default=DEFAULT_QUESTIONS_FILE)
    parser.add_argument("--total-weight", "-w", type=int, help='Total weight of the test', default=9)
    parser.add_argument("--categories", "-c", type=str, nargs='+', help='Categories to include in the test', action='append')
    parser.add_argument("--completely-different", "-d", action='store_true', help='Generate completely different tests (no repeated questions)')
    parser.add_argument("--max-grade", "-g", type=int, help='Maximum grade for the test', default=27)
    parser.add_argument("--verbose", "-v", action='store_true', help='Verbose mode')
    return parser


def parse_args(args = sys.argv[1:]):
    parser = create_arg_parser()
    return parser.parse_args(args)


class TestGenerator:
    def __init__(self, db: QuestionsStore, total_weight: int, target_categories: set[Category],
                 completely_different: bool = False):
        self.__db = db
        self.__total_weight = int(total_weight)
        self.__target_categories = target_categories
        for category in target_categories:
            category = self.__db.category(category)
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
            variables.update(variables_in_category)
        id_to_variables = variables
        variables = {k: (v, self.__db.question(k).weight) for k, v in variables.items()}
        solver.add(sum(w * v for v, w in variables.values()) == self.__total_weight)
        log(" + ".join(f'{q} * {w}' for q, (v, w) in variables.items()), "==", self.__total_weight)
        return solver, id_to_variables

    @property
    def solutions(self):
        while self.__compute_next_solution() == sat:
            yield (solution := self.__solution_to_questions())
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
    