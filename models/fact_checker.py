from pydantic import BaseModel
from typing import List


class FactCheckInput(BaseModel):
    claim: str


class FactCheckOutput(BaseModel):
    sources: List[str]
    conclusion: str
