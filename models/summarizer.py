from pydantic import BaseModel
from typing import List


class SummarizerInput(BaseModel):
    article_text: str


class SummarizerOutput(BaseModel):
    summary_bullets: List[str]
