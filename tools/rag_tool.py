from typing import List, Tuple


class RAGTool:
    def __init__(self):
        # Future: plug into real retriever or API
        pass

    def retrieve_sources(self, claim: str) -> Tuple[List[str], str]:
        """
        Simulated retrieval + conclusion logic
        Returns: (list of sources, conclusion)
        """
        claim = claim.lower()

        if "apple" in claim and "openai" in claim:
            sources = [
                "TechCrunch: Apple reportedly in talks with OpenAI for iOS integration.",
                "The Verge: No official deal confirmed between Apple and OpenAI.",
                "Bloomberg: Sources hint at potential AI collaboration."
            ]
            conclusion = "🤔 Inconclusive. No official confirmation available."
        elif "earth is flat" in claim:
            sources = [
                "NASA: Earth is an oblate spheroid.",
                "Scientific American: Thousands of years of evidence support spherical Earth."
            ]
            conclusion = "❌ Refuted. The claim is false."
        else:
            sources = [
                "No relevant sources found for this claim."
            ]
            conclusion = "❓ Unable to verify the claim with current sources."

        return sources, conclusion
