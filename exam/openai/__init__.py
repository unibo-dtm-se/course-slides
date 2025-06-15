import getpass
import os


KEY_OPENAI_API_KEY = "OPENAI_API_KEY"


def ensure_openai_api_key():
    if not os.environ.get(KEY_OPENAI_API_KEY):
        os.environ[KEY_OPENAI_API_KEY] = getpass.getpass("Enter API key for OpenAI: ")
    return os.environ[KEY_OPENAI_API_KEY]
