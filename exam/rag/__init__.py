from langchain_docling.loader import ExportType, DoclingLoader
from docling_core.transforms.chunker.base import BaseChunk, BaseChunker, BaseMeta
# from docling_core.types.doc.document import ListItem
from langchain_community.embeddings.openai import OpenAIEmbeddings
from langchain_community.vectorstores import SQLiteVec
from exam.openai import ensure_openai_api_key
import re
from exam import DIR_ROOT


DIR_CONTENT = DIR_ROOT / "content"
FILE_DB = DIR_ROOT / "slides-rag.db"
MARKDOWN_FILES = list(DIR_CONTENT.glob("**/*.md"))
REGEX_ITEM_TO_SANITIZE = re.compile(r"\[<\w+ children='([^']*)'>\]")


class SlideChunker(BaseChunker):
    def __item_to_string(self, item):
        if isinstance(item, str):
            return item
        elif hasattr(item, 'text'):
            result = item.text
            if match := REGEX_ITEM_TO_SANITIZE.match(result):
                result = f"{item.marker} {match.group(1)}"
                result = result.replace("\\'", "'")
                return result
            return result
        else:
            raise TypeError(f"Unsupported item type: {type(item)}")

    def __join_into_chunk(self, *items, delim=None):
        if delim is None:
            delim = self.delim
        text = delim.join(self.__item_to_string(item) for item in items)
        return BaseChunk(text=text, meta=BaseMeta())

    def chunk(self, doc, **kwargs):
        skipping = False
        accumulator = []
        for item in doc.texts:
            if item.text.startswith("+++"):
                if skipping:
                    skipping = False
                    accumulator = [] 
                else:
                    skipping = True
            elif skipping:
                continue
            elif item.text.startswith("---"):
                if accumulator:
                    yield self.__join_into_chunk(*accumulator)
                    accumulator = []
            else:
                accumulator.append(item)
        yield self.__join_into_chunk(*accumulator)


def openai_embeddings(model):
    ensure_openai_api_key()
    model = model.lower() if model else "small"
    # https://platform.openai.com/docs/models/
    if "small" in model:
        model = "text-embedding-3-small"
    elif "large" in model:
        model = "text-embedding-3-large"
    elif "old" in model or "ada" in model:
        model = "text-embedding-ada-002"
    else:
        raise ValueError(f"Unknown OpenAI model: {model}. "
                         "Please use 'small', 'large', or 'old'/'ada' variants.")
    return OpenAIEmbeddings(model=model)


def sqlite_vector_store(
        db_file: str = str(FILE_DB), 
        model: str = None, 
        table_name: str = "se_slides"):
    embeddings = openai_embeddings(model)
    return SQLiteVec(
        db_file=db_file,
        embedding=embeddings,
        table=table_name,
        connection=None,
    )
