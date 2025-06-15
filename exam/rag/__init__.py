from langchain_community.embeddings.openai import OpenAIEmbeddings
from langchain_community.vectorstores import SQLiteVec
from exam.openai import ensure_openai_api_key
from exam import DIR_ROOT
from pydantic import BaseModel
import re


DIR_CONTENT = DIR_ROOT / "content"
FILE_DB = DIR_ROOT / "slides-rag.db"
MARKDOWN_FILES = list(DIR_CONTENT.glob("**/_index.md"))
REGEX_SLIDE_DELIMITER = re.compile(r"^\s*(---|\+\+\+)")


class Slide(BaseModel):
    content: str
    source: str
    lines: tuple[int, int]
    index: int

    @property
    def lines_count(self):
        return self.content.count("\n") + 1 if self.content else 0


def all_slides(files = None):
    if files is None:
        files = MARKDOWN_FILES
    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            slide_beginning_line_num = 0
            line_number = 0
            slide_lines = []
            slide_index = 0
            last_was_blank = False
            for line in f.readlines():
                line_number += 1
                if REGEX_SLIDE_DELIMITER.match(line):
                    if slide_lines:
                        yield Slide(
                            content="\n".join(slide_lines),
                            source=str(file.relative_to(DIR_CONTENT)),
                            lines=(slide_beginning_line_num, line_number - 1),
                            index=slide_index,
                        )
                        slide_index += 1
                    slide_lines = []
                    slide_beginning_line_num = line_number + 1
                else:
                    if (stripped := line.strip()) or not last_was_blank:
                        slide_lines.append(line.rstrip())
                    last_was_blank = not stripped
            yield Slide(
                content="\n".join(slide_lines),
                source=str(file.relative_to(DIR_CONTENT)),
                lines=(slide_beginning_line_num, line_number - 1),
                index=slide_index,
            )


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
