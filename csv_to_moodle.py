import csv
import xml
from dataclasses import dataclass
import xml.etree.ElementTree as xml


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
        xml.SubElement(questiontext, "text").text = self.text
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
        reader = csv.DictReader(csvfile, delimiter=";")
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


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} path/to/file.csv")
        sys.exit(1)

    questions = load_questions_from_csv(sys.argv[1])
    questions_by_category = group_by_category(questions)
    categories = sorted(questions_by_category.keys(), key=lambda x: x.name)
    quiz = xml.Element("quiz")
    for category in categories:
        category.to_xml(quiz)
        for question in questions_by_category[category]:
            question.to_xml(quiz)
    tree = xml.ElementTree(quiz)
    tree.write(sys.stdout, encoding="unicode", xml_declaration=True)
