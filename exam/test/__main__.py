import sys

from exam import *
import exam.test as etest


args = etest.parse_args()
questions = QuestionsStore(args.questions_file)

if not args.categories:
    categories_by_index = dict()
    categories = questions.categories
    categories.sort(key=lambda x: questions.category_weight(x), reverse=True)
    for i, category in enumerate(categories):
        print(f"{i + 1})", category.name, f"({questions.category_size(category)} questions, total weight: {questions.category_weight(category)})")
        categories_by_index[i + 1] = category
    input_categories = input("Enter categories to include in the test (space separated): ")
    selected_categories = []
    for i in input_categories.split():
        if "-" in i:
            start, end = i.split("-")
            selected_categories.extend(range(int(start), int(end) + 1))
        else:
            selected_categories.append(int(i))
    indexes = map(int, selected_categories)
    args.categories = {categories_by_index[i] for i in indexes}
elif isinstance(args.categories[0], list):
    args.categories = args.categories[0]

etest.VERBOSE = args.verbose
generator = etest.TestGenerator(
    questions,
    args.total_weight,
    args.categories,
    completely_different=args.completely_different,
    different_categories=args.different_categories,
    min_questions=args.min_questions,
)
etest.log("generating test for topics", args.categories)
print("---")


def questions_in_display_order(test):
    return [
        question
        for category in test.categories
        for question in test.questions_in_category(category)
    ]


kept_question_ids = set()
test = generator.next_solution()
while test is not None:
    test.total_weight = args.max_grade
    print(test)
    print("---")
    displayed_questions = questions_in_display_order(test)
    questions_by_index = {
        index: question
        for index, question in enumerate(displayed_questions, start=1)
    }

    while True:
        try:
            command = input(
                "Next test (Enter for any different set; "
                "'no Q1 Q3-Q5'; 'keep Q2'; or combine both): "
            )
        except (EOFError, KeyboardInterrupt):
            exit(0)

        try:
            no_indexes, keep_indexes = etest.parse_question_commands(
                command,
                len(displayed_questions),
            )
            excluded_ids = {questions_by_index[index].id for index in no_indexes}
            requested_kept_ids = {questions_by_index[index].id for index in keep_indexes}
            next_kept_ids = kept_question_ids | requested_kept_ids
            conflicting_ids = excluded_ids & next_kept_ids
            if conflicting_ids:
                raise ValueError("A previously kept question cannot be replaced")
            if args.completely_different and (next_kept_ids or (excluded_ids and len(excluded_ids) < len(displayed_questions))):
                raise ValueError(
                    "'keep' and partial 'no' commands are incompatible with --completely-different"
                )
        except ValueError as error:
            print(f"Invalid request: {error}", file=sys.stderr)
            continue

        retained_ids = set()
        if excluded_ids:
            retained_ids = {question.id for question in displayed_questions} - excluded_ids
        next_test = generator.next_solution(
            required_question_ids=next_kept_ids | retained_ids,
            excluded_question_ids=excluded_ids,
        )
        if next_test is None:
            if not command.strip():
                test = None
                break
            print("No question set matches that request; try different constraints.", file=sys.stderr)
            continue

        kept_question_ids = next_kept_ids
        test = next_test
        print("---")
        break
print("No more tests")
