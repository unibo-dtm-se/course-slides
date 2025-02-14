from exam import *
import sys


questions = QuestionsStore(sys.argv[1] if len(sys.argv) > 1 else DEFAULT_QUESTIONS_FILE)
tree = questions.to_xml()
tree.write(sys.stdout, encoding="unicode", xml_declaration=True)
