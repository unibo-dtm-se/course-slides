from exam import *
from exam.solution import SolutionProvider


questions = QuestionsStore()
llm = SolutionProvider()


for q in questions.questions:
    print(q.id)
    print("\t", q.text)
    a = llm.answer(q)
    print("\t", a.answer.replace("\n", "\n \t"))
    print("\t", f"Score: {a.score:.2f}")
    print("---")
    try:
        input("Press enter to continue")
    except (EOFError, KeyboardInterrupt):
        exit(0)
