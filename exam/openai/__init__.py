import getpass
import os
from langchain.chat_models import init_chat_model


KEY_OPENAI_API_KEY = "OPENAI_API_KEY"


def ensure_openai_api_key():
    if not os.environ.get(KEY_OPENAI_API_KEY):
        os.environ[KEY_OPENAI_API_KEY] = getpass.getpass("Enter API key for OpenAI: ")
    return os.environ[KEY_OPENAI_API_KEY]


def llm_client(model_name: str = None, model_provider: str = None, structured_output: type = None):
    if not model_name:
        model_name = "gpt-4o-mini"
    if not model_provider:
        model_provider = "openai"
    ensure_openai_api_key()
    llm = init_chat_model(model_name, model_provider=model_provider)
    if structured_output is not None:
        llm = llm.with_structured_output(structured_output)
    return llm, model_name, model_provider


class AIOracle:
    def __init__(self, model_name: str = None, model_provider: str = None, structured_output: type = None):
        self.__llm, self.__model_name, self.__model_provider = llm_client(model_name, model_provider, structured_output)

    @property
    def llm(self):
        return self.__llm

    @property
    def model_name(self):
        return self.__model_name

    @property
    def model_provider(self):
        return self.__model_provider
