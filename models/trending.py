from pydantic import BaseModel


class TrendingNewsInput(BaseModel):
    topic: str


class TrendingNewsOutput(BaseModel):
    headlines: list[str]
