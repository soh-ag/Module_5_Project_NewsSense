from typing import List


class WebSearchTool:
    def __init__(self):
        # Future: connect to real API like SerpAPI
        pass

    def search(self, topic: str) -> List[str]:
        topic = topic.lower()

        if "ai" in topic:
            return [
                "Meta introduces Llama 3 model with major improvements",
                "OpenAI and Apple rumored to collaborate on AI assistant",
                "Google launches new Gemini update in Android"
            ]
        elif "politics" in topic:
            return [
                "Debate over digital voting heats up",
                "Opposition party announces shadow cabinet",
                "International observers question election fairness"
            ]
        else:
            return [
                "Global warming surpasses record levels in 2025",
                "New research shows rise in remote work productivity",
                "SpaceX plans new lunar mission with international team"
            ]
