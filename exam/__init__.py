import csv
import xml
from dataclasses import dataclass
import xml.etree.ElementTree as xml
from pathlib import Path
from io import StringIO
from markdown import markdown


DIR_ROOT = Path(__file__).parent.parent
DEFAULT_QUESTIONS_FILE = DIR_ROOT / "static" / "questions.csv" 


class IdGenerator:
    def __init__(self):
        self.__categories = dict()

    def id_for(self, category):
        if category not in self.__categories:
            self.__categories[category] = 1
        else:
            self.__categories[category] += 1
        return f"{category}-{self.__categories[category]}"


DEFAULT_ID_GENERATOR = IdGenerator()


@dataclass(unsafe_hash=True)
class Category:
    name: str

    def __post_init__(self):
        self.name = self.name.strip().replace(" ", "")

    def copy(self):
        return Category(self.name)

    def to_xml(self, root: xml.Element):
        if root is None:
            root = xml.Element("question")
        else:
            root = xml.SubElement(root, "question")
        root.set("type", "category")
        category = xml.SubElement(root, "category")
        xml.SubElement(category, "text").text = f'$course$/top/{self.name}'
        info = xml.SubElement(root, "info")
        info.set("format", "html")
        xml.SubElement(info, "text").text = ""
        return root


@dataclass(unsafe_hash=True)
class Question:
    category: Category = Category("Default")
    text: str = ""
    type: str = "essay"
    weight: float = 1.0
    max_lines: int = 15
    id: str = None

    def __post_init__(self):
        if not isinstance(self.category, Category):
            self.category = Category(self.category)
        if self.id is None:
            self.id = DEFAULT_ID_GENERATOR.id_for(self.category.name)
        self.weight = float(self.weight)
        self.max_lines = int(self.max_lines)

    def copy(self):
        return Question(
            category=self.category.copy(),
            text=self.text,
            type=self.type,
            weight=self.weight,
            max_lines=self.max_lines,
            id=self.id,
        )

    def to_xml(self, root: xml.Element):
        if root is None:
            root = xml.Element("question")
        else:
            root = xml.SubElement(root, "question")  
        root.set("type", self.type)
        name = xml.SubElement(root, "name")
        xml.SubElement(name, "text").text = self.id
        questiontext = xml.SubElement(root, "questiontext")
        questiontext.set("format", "html")
        xml.SubElement(questiontext, "text").text = markdown(self.text)
        xml.SubElement(root, "defaultgrade").text = str(float(self.weight))
        xml.SubElement(root, "penalty").text = "0"
        xml.SubElement(root, "hidden").text = "0"
        xml.SubElement(root, "responserequired").text = "1"
        xml.SubElement(root, "responseformat").text = "editor"
        xml.SubElement(root, "responsefieldlines").text = str(int(self.max_lines))
        xml.SubElement(root, "attachments").text = "0"
        xml.SubElement(root, "attachmentsrequired").text = "0"
        return root
    

def load_questions_from_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")
        for row in reader:
            yield Question(
                category=row["Category"],
                text=row["Question"],
                weight=row["Weight"],
            )


def group_by_category(questions):
    questions_by_category = dict()
    for question in questions:
        questions_by_category.setdefault(question.category, []).append(question)
    return questions_by_category


class QuestionsStore:
    def __init__(self, questions=DEFAULT_QUESTIONS_FILE):
        if isinstance(questions, Path) or isinstance(questions, str):
            questions = load_questions_from_csv(questions)
        questions = [q.copy() for q in questions]
        self.__questions_by_category = group_by_category(questions)
        self.__questions_by_id = {q.id: q for question_list in self.__questions_by_category.values() for q in question_list}
        self.__categories = tuple(sorted(self.__questions_by_category.keys(), key=lambda x: x.name))

    @property
    def categories(self):
        return sorted(self.__categories, key=lambda x: x.name)
    
    @property
    def questions(self):
        return sorted(self.__questions_by_id.values(), key=lambda x: x.id)
    
    def category(self, category):
        if not isinstance(category, Category):
            category = Category(category)
        if category not in self.__categories:
            raise KeyError(f"Category {category} not found")
        return category
    
    def question(self, id):
        if id not in self.__questions_by_id:
            raise KeyError(f"Question {id} not found")
        return self.__questions_by_id[id]
    
    def questions_in_category(self, category):
        category = self.category(category)
        return sorted(self.__questions_by_category.get(category, []), key=lambda x: x.id)
    
    def category_size(self, category):
        category = self.category(category)
        return len(self.__questions_by_category.get(category, []))
    
    def category_weight(self, category):
        category = self.category(category)
        return sum(q.weight for q in self.__questions_by_category.get(category, []))
    
    def __len__(self):
        return len(self.questions)
    
    def __total_weight(self):
        return sum(q.weight for q in self.__questions_by_id.values())
    
    @property
    def total_weight(self):
        return self.__total_weight()
    
    @total_weight.setter
    def total_weight(self, value):
        old_weight = self.__total_weight()
        if value == old_weight:
            return
        factor = value / old_weight
        for question in self.questions:
            question.weight *= factor
    
    def to_xml(self, rootname="quiz"):
        quiz = xml.Element(rootname)
        for category in self.categories:
            category.to_xml(quiz)
            for question in self.questions_in_category(category):
                question.to_xml(quiz)
        return xml.ElementTree(quiz)
    
    def __str__(self):
        result = StringIO()
        print(f"# {len(self)} questions, total weight: {self.total_weight:.2f}", file=result)
        for category in self.categories:
            print(f"## {category.name} ({self.category_size(category)} questions, total weight: {self.category_weight(category):.2f})", file=result)
            for question in self.questions_in_category(category):
                print(f"- {question.id} ({question.weight:.2f}): {question.text}", file=result)
        return result.getvalue()
    
    def __repr__(self):
        return f"QuestionsStore({self.questions})"
    
    def __eq__(self, value):
        if not isinstance(value, QuestionsStore):
            return False
        return self.questions == value.questions
    
    def __hash__(self):
        return hash(self.questions)
    