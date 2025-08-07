from typing import List, Optional
from pydantic import BaseModel


class FactCheckResult(BaseModel):
    claim: str
    is_true: bool
    explanation: str
    sources: Optional[List[str]] = []
