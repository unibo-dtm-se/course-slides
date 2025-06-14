from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from langchain.chat_models import init_chat_model


class Answer(BaseModel):
    answer: str = Field(description="Text of the answer to some question in the test, in Markdown.")
    score: float = Field(description="Score for the answer, must be between 0 (totally wrong) and 1 (perfectly correct).", ge=0.0, le=1.0)


def get_prompt(question: str, target_score: float = None):
    if target_score is None:
        target_score = 1.0  # Default to perfect score if not specified
    template = ChatPromptTemplate.from_template(
        "You are a student in the Software Engineering course, for the Digital Transformantion and Management master programme.\n"
        "Your task is to provide an answer to the following question, which is part of a written test, "
        "which you have to pass in order to pass the exam for the course.\n"
        "You're tergetting a score of more or less {target_score_pecent} for your answer, "
        "where 0% meanse completely idiotic, and 100% means perfect and complete.\n"
        "Only extract the properties mentioned in the '{class_name}' function.\n"
        "Question is below:\n\n"
        "{question}" 
    )
    return template.invoke({
        "class_name": Answer.__name__,
        "target_score_pecent": target_score * 100,
        "question": question
    })


def llm_client(model_name: str = None, model_provider: str = None):
    if not model_name:
        model_name = "gpt-4o-mini"
    if not model_provider:
        model_provider = "openai"
    llm = init_chat_model(model_name, model_provider=model_provider)
    return llm.with_structured_output(Answer)


class SolutionProvider:
    def __init__(self, model_name: str = None, model_provider: str = None):
        self.__llm = llm_client(model_name, model_provider)

    def answer(self, question, target_score: float = None) -> Answer:
        text = question if isinstance(question, str) else question.text
        prompt = get_prompt(text, target_score)
        result = self.__llm.invoke(prompt)
        if isinstance(result, Answer):
            return result
        else:
            raise ValueError(f"Expected Answer, got {type(result)}: {result}")
