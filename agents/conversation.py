from agents.trending import TrendingNewsAgent


class ConversationAgent:
    def __init__(self):
        self.trending_agent = TrendingNewsAgent()
        pass  # future logging/setup

    def handle(self, user_input: str) -> str:
        intent = self.detect_intent(user_input)

        if intent == "get_trending":
            return self.get_trending_news()
        elif intent == "verify_claim":
            return self.verify_claim()
        elif intent == "summarize_news":
            return self.summarize_news()
        else:
            return "Sorry, I didn't understand your request."

    def detect_intent(self, text: str) -> str:
        # 🧪 Dummy logic – Replace with real intent classifier later
        text = text.lower()
        if "trending" in text or "happening" in text:
            return "get_trending"
        elif "true" in text or "verify" in text or "did" in text:
            return "verify_claim"
        elif "summarize" in text or "summary" in text:
            return "summarize_news"
        else:
            return "unknown"

    def get_trending_news(self) -> str:
            # Future: pass topic from user input
        results = self.trending_agent.get_trending_news("AI")
        return "\n".join(results)

    def verify_claim(self) -> str:
        return "[Fact Check] ❌ No official source confirms this claim."

    def summarize_news(self) -> str:
        return "[Summary] • Point 1\n• Point 2\n• Point 3"
