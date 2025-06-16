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
    indexes = map(int, input_categories.split())
    args.categories = {categories_by_index[i] for i in indexes}

etest.VERBOSE = args.verbose
generator = etest.TestGenerator(questions, args.total_weight, args.categories, args.completely_different)
etest.log("generating test for topics", [c.name for c in args.categories])
print("---")
for test in generator.solutions:
    test.total_weight = args.max_grade
    print(test)
    print("---")
    try:
        input("Press enter for next test")
    except (EOFError, KeyboardInterrupt):
        exit(0)
print("No more tests")
