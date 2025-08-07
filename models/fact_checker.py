from pydantic import BaseModel, Field
from typing import List


class FactCheckInput(BaseModel):
    claim: str


class FactCheckOutput(BaseModel):
    sources: List[str]
    conclusion: str
