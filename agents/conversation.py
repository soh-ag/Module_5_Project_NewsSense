from agents.trending import TrendingNewsAgent
from agents.fact_checker import FactCheckerAgent
from agents.summarizer import NewsSummarizerAgent
from typing import List


class ConversationAgent:
    def __init__(self):
        self.trending_agent = TrendingNewsAgent()
        self.fact_checker = FactCheckerAgent()
        self.summarizer_agent = NewsSummarizerAgent()


        pass  # future logging/setup

    def handle(self, user_input: str) -> str:
        intent = self.detect_intent(user_input)

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
        results = self.trending_agent.get_trending_news(topic)
        return "\n".join(results)

    def verify_claim(self, user_input: str) -> str:
        # Future: extract actual claim from user_input
        # claim = "Is OpenAI partnering with Apple?"
        return self.fact_checker.verify_claim(user_input)
        # results = self.fact_checker.verify_claim("claim")
        # return "\n".join(results)

    def summarize_news(self, user_input: str) -> str:
        return self.summarizer_agent.summarize_news(user_input)

    def extract_topic(self, text: str) -> str:
        # Future: use LLM or keyword extractor
        # Now: manually extract based on keywords
        text = text.lower()
        if "ai" in text:
            return "AI"
        elif "politics" in text:
            return "politics"
        else:
            return "general"    