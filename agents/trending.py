from typing import List
from tools.web_search import WebSearchTool


class TrendingNewsAgent:
    def __init__(self):
        # future scope: add logfire or config
        self.search_tool = WebSearchTool()
        pass

    def get_trending_news(self, topic: str = "general", ) -> List[str]:
        return self.search_tool.search(topic)