from typing import List


class TrendingNewsAgent:
    def __init__(self):
        # future scope: add logfire or config
        pass

    def get_trending_news(self, topic: str = "general") -> List[str]:
        """
        Dummy implementation to simulate trending news.
        Future: replace with real web search or news API.
        """
        topic = topic.lower()

        if "ai" in topic:
            return [
                "Meta releases new LLM for public use.",
                "Elon Musk's xAI announces Grok-2 model.",
                "Google DeepMind introduces Gemini Pro updates."
            ]
        elif "politics" in topic:
            return [
                "Elections 2025: Campaigns intensify nationwide.",
                "Debate over digital voting continues.",
                "New policies spark protests in capital."
            ]
        else:
            return [
                "NASA plans new moon mission by 2026.",
                "Global stock markets show signs of recovery.",
                "Climate change report urges immediate action."
            ]
