from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from langchain.chat_models import init_chat_model
from exam import DIR_ROOT, Question
from exam.openai import ensure_openai_api_key
from exam.rag import sqlite_vector_store
from yaml import safe_dump, safe_load


FILE_TEMPLATE = DIR_ROOT / "exam" / "solution" / "prompt-template.txt"
DIR_SOLUTIONS = DIR_ROOT / "solutions"
DIR_SOLUTIONS.mkdir(exist_ok=True)


class Answer(BaseModel):
    should: list[str] = Field(
        description="List of features that the perfect answer should contain. Each item is a Markdown string line.",
    )
    examples: list[str] = Field(
        description="List of examples that the perfect answer may contain. Each item is a Markdown string line.",
    )
    should_not: list[str] = Field(
        description="List of features that the perfect answer should not contain (e.g. common errors). Each item is a Markdown string line.",
    )
    see_also: list[str] = Field(
        description="List of relevant background/contextual/motivational aspects that should be mentioned in the answer. Each item is a Markdown string line.",
    )

    def pretty(self, indent=0, prefix="\t") -> str:
        result = "Should:\n"
        if self.should:
            result += "\n".join(f"- {item}" for item in self.should) + "\n"
        else:
            result += "- <none>\n"
        result += "Should not:\n"
        if self.should_not: 
            result += "\n".join(f"- {item}" for item in self.should_not) + "\n"
        else:
            result += "- <none>\n"
        result += "Examples:\n"
        if self.examples:
            result += "\n".join(f"- {item}" for item in self.examples) + "\n"
        else:
            result += "- <none>\n"
        result += "Other aspects to be mentioned:\n"
        if self.see_also:
            result += "\n".join(f"- {item}" for item in self.see_also) + "\n"
        else:
            result += "- <none>\n"
        result = result.strip()
        if indent > 0:
            result = (indent * prefix) + result.replace("\n", "\n" + indent * prefix)
        return result


TEMPLATE = FILE_TEMPLATE.read_text(encoding="utf-8")


def get_prompt(question: str, *helps: str):
    template = ChatPromptTemplate.from_template(TEMPLATE)
    return template.invoke({
        "class_name": Answer.__name__,
        "question": question,
        "help": "\n\n".join(helps) if helps else "",
    })


def llm_client(model_name: str = None, model_provider: str = None):
    if not model_name:
        model_name = "gpt-4o-mini"
    if not model_provider:
        model_provider = "openai"
    ensure_openai_api_key()
    llm = init_chat_model(model_name, model_provider=model_provider)
    return llm.with_structured_output(Answer), model_name, model_provider


class SolutionProvider:
    def __init__(self, model_name: str = None, model_provider: str = None):
        self.__llm, self.__model_name, self.__model_provider = llm_client(model_name, model_provider)
        self.__vector_store = sqlite_vector_store()
        self.__use_helps = self.__vector_store.get_dimensionality() > 0

    def answer(self, question: Question, max_helps=5) -> Answer:
        cache_file = DIR_SOLUTIONS / f"{question.id}.yaml"
        if cache_file.exists():
            with open(cache_file, "r", encoding="utf-8") as f:
                print(f"# loading cached answer from {cache_file}")
                try:
                    cached_answer = safe_load(f)
                    return Answer(
                        answer=cached_answer["answer"], 
                        score=cached_answer["score"],
                    )
                except Exception as e:
                    print(f"# error loading cached answer from {cache_file}: {e}")
                    cache_file.unlink()
        text = question.text
        helps = []
        if self.__use_helps:
            helps = [doc.page_content for doc in self.__vector_store.similarity_search(text, k=max_helps)]
        prompt = get_prompt(text, *helps)
        result = self.__llm.invoke(prompt)
        if isinstance(result, Answer):
            with open(cache_file, "w", encoding="utf-8") as f:
                print(f"# saving answer to {cache_file}")
                yaml = result.model_dump()
                yaml["question"] = text
                yaml["helps"] = helps
                yaml["id"] = question.id
                yaml["model_name"] = self.__model_name
                yaml["model_provider"] = self.__model_provider
                yaml["prompt_template"] = TEMPLATE
                safe_dump(yaml, f, sort_keys=True, allow_unicode=True)
            return result
        else:
            raise ValueError(f"Expected Answer, got {type(result)}: {result}")
