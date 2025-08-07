from my_agents.trending import TrendingNewsAgent
from my_agents.fact_checker import FactCheckerAgent
from my_agents.summarizer import NewsSummarizerAgent
from typing import List
import logfire



class ConversationAgent:
    def __init__(self):
        self.trending_agent = TrendingNewsAgent()
        self.fact_checker = FactCheckerAgent()
        self.summarizer_agent = NewsSummarizerAgent()

    @logfire.instrument()
    def handle(self, user_input: str) -> str:
        intent = self.detect_intent(user_input)
        logfire.info("Intent detected", input=user_input, intent=intent)

        if intent == "get_trending":
            return self.get_trending_news(user_input)
        elif intent == "verify_claim":
            return self.verify_claim(user_input)
        elif intent == "summarize_news":
            return self.summarize_news(user_input)
        else:
            return "Sorry, I didn't understand your request."

    def detect_intent(self, text: str) -> str:
        text = text.lower()
        if any(kw in text for kw in ["summarize", "summary", "summarise", "short version", "compress", "bullet"]):
            return "summarize_news"
        elif any(kw in text for kw in ["verify", "true", "false", "did", "does", "is ", "are ", "claim", "real"]):
            return "verify_claim"
        elif any(kw in text for kw in ["trending", "happening", "what's new", "latest", "news"]):
            return "get_trending"
        else:
            return "unknown"

    def get_trending_news(self, user_input: str) -> str:
        topic = self.extract_topic(user_input)
        return "\n".join(self.trending_agent.get_trending_news(topic))

    def verify_claim(self, user_input: str) -> str:
        return self.fact_checker.verify_claim(user_input)

    def summarize_news(self, user_input: str) -> str:
        return self.summarizer_agent.summarize_news(user_input)

    def extract_topic(self, text: str) -> str:
        text = text.lower()
        if "ai" in text:
            return "AI"
        elif "politics" in text:
            return "politics"
        else:
            return "general"