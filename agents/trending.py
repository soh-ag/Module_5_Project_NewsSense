import logfire
from typing import List
from tools.web_search import WebSearchTool
from models.trending import TrendingNewsInput, TrendingNewsOutput

class TrendingNewsAgent:
    def __init__(self):
        self.search_tool = WebSearchTool()

    @logfire.instrument()
    def get_trending_news(self, topic: str = "general") -> list[str]:
        logfire.info("Fetching trending news", topic=topic)
        input_data = TrendingNewsInput(topic=topic)
        headlines = self.search_tool.search(input_data.topic)
        logfire.info("Headlines fetched", count=len(headlines))
        output_data = TrendingNewsOutput(headlines=headlines)
        return output_data.headlines