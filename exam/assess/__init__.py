from exam import QuestionsStore, Question, DIR_ROOT
from exam.solution import Answer, load_cache
from pathlib import Path
import re


ALL_QUESTIONS = QuestionsStore()
PATTERN_QUESTION_FOLDER = re.compile(r"^Q\d+\s+-\s+(\w+-\d+)$")
FILE_TEMPLATE = DIR_ROOT / "exam" / "assess" / "prompt-template.txt"
TEMPLATE = FILE_TEMPLATE.read_text(encoding="utf-8")


def _load_exam(exam: Path | str | list[str] | QuestionsStore) -> QuestionsStore:
    if isinstance(str):
        exam = Path(exam)
    if isinstance(exam, Path):
        questions = [d.name for d in exam.glob("Q* - *") if d.is_dir()]
        exam = []
        for question in questions:
            match = PATTERN_QUESTION_FOLDER.match(question)
            if match:
                exam.append(match.group(1))
    if isinstance(exam, list):
        if exam:
            exam = ALL_QUESTIONS.sample(*exam)
        else:
            raise ValueError("No question ID has been found or none was provided")
    if isinstance(exam, QuestionsStore):
        return exam
    else:
        raise TypeError("Exam must be a Path, str, list of question IDs, or QuestionsStore instance")


class Assesser:
    def __init__(self, exam: Path | str | list[str] |QuestionsStore):
        self.__exam: QuestionsStore = _load_exam(exam)
        self.__answers: dict[str, Answer] = {}
        for question in self.__exam.questions:
            if (cached_answer := load_cache(question)):
                self.__answers[question.id] = cached_answer
            else:
                raise ValueError(f"Cached answer for question {question.id} not found")

    def assess(self):
        raise NotImplementedError("This method should be overridden by subclasses")

    def get_results(self):
        raise NotImplementedError("This method should be overridden by subclasses")