from exam.assess import *
import sys


path = sys.argv[1] if len(sys.argv) > 1 else None
if not path:
    raise ValueError("Please provide the path to the exam directory")

assessor = Assessor(path)
assessments = assessor.assess_all()
assessments.pretty_print()
