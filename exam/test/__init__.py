import argparse
import sys
from exam import *
from constraint import *


VERBOSE = True


def log(*args):
    if VERBOSE:
        print("i:", *args, file=sys.stderr)


def create_arg_parser():
    parser = argparse.ArgumentParser(description='Test Generator')
    parser.add_argument("--verbose", "-v", action='store_true', help='Verbose mode')
    parser.add_argument("--questions-file", "-q", type=str, help='Path to questions .csv file', default=DEFAULT_QUESTIONS_FILE)
    parser.add_argument("--total-weight", "-w", type=int, help='Total weight of the test', default=27)
    parser.add_argument("--categories", "-c", type=str, nargs='+', help='Categories to include in the test', action='append')
    return parser


def parse_args(args = sys.argv[1:]):
    parser = create_arg_parser()
    return parser.parse_args(args)


class TestGenerator:
    def __init__(self, db: QuestionsStore, total_weight: int, target_categories: set[Category]):
        self.__db = db
        self.__total_weight = int(total_weight)
        self.__target_categories = target_categories
        for category in target_categories:
            category = self.__db.category(category)
            assert self.__db.category_size(category) > 0, f"Category {category} is empty"
            assert self.__db.category_weight(category) > 0, f"Category {category} has no weight"
        self.__problem = self.__configure_problem()

    def __configure_problem(self):
        problem = Problem()
        question_ids = []
        for category in self.__target_categories: # in self.__db.categories:
            question_ids_in_category = []
            for question in self.__db.questions_in_category(category): 
                problem.addVariable(question.id, [0, 1])
                question_ids_in_category.append(question.id)
            if category in self.__target_categories:
                problem.addConstraint(MinSumConstraint(1), question_ids_in_category)
                log(" + ".join(question_ids_in_category), ">= 1")
            # else:
            #     problem.addConstraint(MaxSumConstraint(0), variables)
            #     log(" + ".join(variables), "== 0")
            question_ids.extend(question_ids_in_category)
        weights = [self.__db.question(q).weight for q in question_ids]
        problem.addConstraint(ExactSumConstraint(self.__total_weight, weights), question_ids)
        log(" + ".join(f'{q} * {w}' for q, w in zip(question_ids, weights)), "==", self.__total_weight)
        return problem

    @property
    def solutions(self):
        iter = self.__problem.getSolutionIter()
        while (solution := self.__compute_next_solution(iter)) is not None:
            yield self.__solution_to_questions(solution)

    def __compute_next_solution(self, iter):
        log("computing next solution...")
        return next(iter, None)
    
    def __solution_to_questions(self, solution):
        questions = []
        for question_id, value in solution.items():
            if value == 1:
                questions.append(self.__db.question(question_id))
        return QuestionsStore(questions)
    