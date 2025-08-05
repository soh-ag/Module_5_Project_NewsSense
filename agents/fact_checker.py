from tools.rag_tool import RAGTool


class FactCheckerAgent:
    def __init__(self):
        # Future: Connect real RAG tool or search engine
        self.rag_tool = RAGTool()
        pass

    def verify_claim(self, claim: str) -> str:
        sources, conclusion = self.rag_tool.retrieve_sources(claim)
        sources_text = "\n".join(f"🔗 {s}" for s in sources)
        return f"{sources_text}\n\n🧾 Conclusion: {conclusion}"
