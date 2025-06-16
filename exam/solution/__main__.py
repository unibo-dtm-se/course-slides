from exam import *
from exam.solution import SolutionProvider
import sys


questions = QuestionsStore()
llm = SolutionProvider()

if len(sys.argv) > 1:
    targets = [questions.question(id.strip()) for id in sys.argv[1:]]
else:
    targets = questions.questions

for q in targets:
    print(q.id)
    print("\t", q.text)
    a = llm.answer(q)
    print(a.pretty(indent=1))
    print("---")
    
print("Done.")
