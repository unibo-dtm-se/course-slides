from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from langchain.chat_models import init_chat_model
from exam import DIR_ROOT, Question
from exam.openai import ensure_openai_api_key
from exam.rag import sqlite_vector_store
from yaml import safe_dump, safe_load


DIR_SOLUTIONS = DIR_ROOT / "solutions"
DIR_SOLUTIONS.mkdir(exist_ok=True)


class Answer(BaseModel):
    answer: str = Field(description="Text of the answer to some question in the test, in Markdown.")
    score: float = Field(description="Score for the answer, must be between 0 (totally wrong) and 1 (perfectly correct).", ge=0.0, le=1.0)


TEMPLATE = (
    "You are a student in the Software Engineering course, for the Digital Transformantion and Management master programme.\n"
    "Your task is to provide an answer to the following question, which is part of a written test, "
    "which you have to pass in order to pass the exam for the course.\n"
    "The teacher asks to provide examples, background, and context even if the question does not explicitly ask for it.\n"
    "You're tergetting a score of more or less {target_score_pecent} for your answer, "
    "where 0% meanse completely idiotic, and 100% means perfect and complete.\n"
    "Only extract the properties mentioned in the '{class_name}' function.\n"
    "Question is:\n"
    "\t{question}\n\n" 
    "Below are snippets from the course material that may help you answer the question:\n\n"
    "{help}"
)


def get_prompt(question: str, target_score: float = None, *helps: str):
    if target_score is None:
        target_score = 1.0  # Default to perfect score if not specified
    template = ChatPromptTemplate.from_template(TEMPLATE)
    return template.invoke({
        "class_name": Answer.__name__,
        "target_score_pecent": target_score * 100,
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

    def answer(self, question: Question, target_score: float = None, k=5) -> Answer:
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
            helps = [doc.page_content for doc in self.__vector_store.similarity_search(text, k=k)]
        prompt = get_prompt(text, target_score, *helps)
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
                yaml["target_score"] = target_score
                yaml["prompt_template"] = TEMPLATE
                safe_dump(yaml, f, sort_keys=True, allow_unicode=True)
            return result
        else:
            raise ValueError(f"Expected Answer, got {type(result)}: {result}")
