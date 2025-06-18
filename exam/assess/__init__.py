from exam import QuestionsStore, Question, DIR_ROOT
from exam.openai import AIOracle
from exam.solution import Answer, load_cache as load_answer
from pathlib import Path
from pydantic import BaseModel, Field
from enum import Enum
from yaml import safe_dump, safe_load
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


class FeatureType(str, Enum):
    """Enumeration of feature types that can be assessed in a question's answer."""
    EXAMPLE = "example"
    SHOULD = "mandatory mention"
    SHOULDNT = "mistake"
    SEE_ALSO = "optional mention"


class Feature(BaseModel):
    type: FeatureType = Field(description="Type of the feature being assessed (e.g. example, mandatory mention, mistake, optional mention)")
    description: str = Field(description="Natural language description of the feature being assessed")

    @property
    def verb_ideal(self) -> str:
        if self.type == FeatureType.SHOULDNT:
            return "should be present"
        return "should be absent"

    @property
    def verb_actual(self) -> str:
        if self.type == FeatureType.SHOULDNT:
            return "is actually present"
        return "is actually absent"


def enumerate_features(answer: Answer):
    if not answer:
        return
    i = 0
    for should in answer.should:
        yield i, Feature(type=FeatureType.SHOULD, description=should)
        i += 1
    for shouldnt in answer.shouldnt:
        yield i, Feature(type=FeatureType.SHOULDNT, description=shouldnt)
        i += 1
    for example in answer.examples:
        yield i, Feature(type=FeatureType.EXAMPLE, description=example)
        i += 1
    for see_also in answer.see_also:
        yield i, Feature(type=FeatureType.SEE_ALSO, description=see_also)
        i += 1


class FeatureAssessment(BaseModel):
    satisfied: bool = Field(description="Whether the feature is present (if it should be present) or lacking (if it shouldn't be present)")
    motivation: str = Field(description="Explanation of why the feature is present or not")


class AnswerAssessment(BaseModel):
    answer: str = Field(description="The student's answer to the question")
    assessment: dict[Feature, FeatureAssessment] = Field(
        description="Dictionary of feature assessments keyed by feature, each containing presence and motivation"
    )


class StudentAssessment(BaseModel):
    name: str = Field(description="Name of the student")
    code: str = Field(description="ID of the student, e.g. student number or email address")
    answers: dict[Question, AnswerAssessment] = Field(
        description="Dictionary of answers keyed by question ID, each containing the student's answer and its assessment"
    )


class TestAssessment:
    def __init__(self):
        self.__students_by_name: dict[str, StudentAssessment] = {}
        self.__students_by_code: dict[str, StudentAssessment] = {}

    def add_assessment(self, code: str, name: str, question: Question, answer: str, feature: Feature, assessment: FeatureAssessment):
        if name not in self.__students_by_name:
            instance = StudentAssessment(
                name=name,
                code=code,
                answers={},
            )
            self.__students_by_name[name] = instance
            self.__students_by_code[code] = instance
        instance = self.__students_by_name[name]
        if question not in instance.answers:
            instance.answers[question] = AnswerAssessment(
                answer=answer,
                assessment={},
            )
        instance.answers[question].assessment[feature] = assessment

    @property
    def assessments(self) -> list[StudentAssessment]:
        return list(self.__students_by_name.values())

    def pretty_print(self):
        for index, name in enumerate(sorted(self.__students_by_name)):
            student = self.__students_by_name[name]
            print(f"Student: {student.name} ({student.code})")
            for question, answer in student.answers.items():
                print(f"  Question: {question.text}")
                print(f"  Answer:\n\t{answer.answer.replace('\n', '\n\t')}")
                for feature, assessment in answer.assessment.items():
                    print(f"    - [{'ok' if assessment.satisfied else 'KO'}] {feature.type.name}: {feature.description}")
                    print(f"        * {assessment.motivation.replace('\n', '\n          ')}")
            if index > 0:
                print("---")


def first(iterable):
    """Return the first item of an iterable or None if it's empty."""
    return next(iter(iterable), None)


class Assessor(AIOracle):
    def __init__(self, exam_dir_by_questions: Path, model_name: str = None, model_provider: str = None):
        super().__init__(model_name, model_provider, FeatureAssessment)
        self.__root = Path(exam_dir_by_questions)
        self.__exam: QuestionsStore = _load_exam(exam_dir_by_questions)
        self.__answers: dict[str, Answer] = {}
        for question in self.__exam.questions:
            if (cached_answer := load_answer(question)):
                self.__answers[question.id] = cached_answer
            else:
                raise ValueError(f"Cached answer for question {question.id} not found")

    def __iterate_over_answers(self):
        for question in self.__exam.questions:
            target = self.__answers.get(question.id)
            for dir in self.__root.glob(f"Q* - {question.id}/*"):
                if dir.is_dir():
                    code, name = dir.name.split(" - ")[:2]
                    attempt_file = first(dir.glob("Attempt*_textresponse"))
                    answer = attempt_file.read_text(encoding="utf-8") if attempt_file else None
                    yield (code, name, question, target, answer, dir)

    def __save_cache(self, dir: Path, feature: Feature, assessment: FeatureAssessment, index: int):
        if not dir:
            return
        cache_file = dir / f"feature_{index}_{feature.type.name}.yml"
        cache_data = assessment.model_dump()
        cache_data["feature"] = feature.description
        cache_data["feature_type"] = feature.type.name
        safe_dump(cache_data, cache_file.open("w", encoding="utf-8"))
        print(f"# saved assessment to {cache_file}")

    def __load_cache(self, dir: Path, feature: Feature, index: int) -> FeatureAssessment | None:
        if not dir:
            return None
        cache_file = dir / f"feature_{index}_{feature.type.name}.yml"
        if not cache_file.exists():
            return None
        with cache_file.open("r", encoding="utf-8") as f:
            try:
                cached_data = safe_load(f)
                return FeatureAssessment(
                    motivation=cached_data.get("motivation"),
                    satisfied=cached_data.get("satisfied", False),
                )
            except Exception as e:
                print(f"# error loading cached assessment from {cache_file}: {e}")
                cache_file.unlink()


    def __assess_feature(self, question: Question, feature: Feature, answer: str, dir: Path, index: int) -> FeatureAssessment:
        cached_assessment = self.__load_cache(dir, feature, index)
        if cached_assessment:
            print(f"# loaded cached assessment for {feature.type.name} from {dir}")
            return cached_assessment
        prompt = TEMPLATE.format(
            class_name=FeatureAssessment.__name__,
            question=question.text,
            feature_type=feature.type.value,
            feature_verb_ideal=feature.verb_ideal,
            feature_verb_actual=feature.verb_actual,
            feature=feature.description,
            answer=answer
        )
        result = self.llm.invoke(prompt)
        if not isinstance(result, FeatureAssessment):
            raise TypeError(f"Expected {FeatureAssessment.__name__}, got {type(result)}")
        self.__save_cache(dir, feature, result, index)
        return result

    def assess_all(self):
        assessments = TestAssessment()
        for code, name, question, target, answer, dir in self.__iterate_over_answers():
            for index, feature in enumerate_features(target):
                assessment = self.__assess_feature(question, feature, answer, dir, index)
                assessments.add_assessment(code, name, question, answer, feature, assessment)
        return assessments
