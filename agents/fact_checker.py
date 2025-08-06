import logfire
from tools.rag_tool import RAGTool
from models.fact_checker import FactCheckInput, FactCheckOutput


class FactCheckerAgent:
    def __init__(self, rag_tool):
        self.rag_tool = rag_tool

    @logfire.instrument()
    def verify_claim(self, claim: str) -> str:
        logfire.info("Verifying claim", claim=claim)
        validated_input = FactCheckInput(claim=claim)
        sources, conclusion = self.rag_tool.retrieve_sources(validated_input.claim)
        validated_output = FactCheckOutput(sources=sources, conclusion=conclusion)
        logfire.info("Fact check result", sources_found=len(sources), conclusion=conclusion)
        sources_text = "\n".join(f"🔗 {s}" for s in validated_output.sources)
        return f"{sources_text}\n\n🧾 Conclusion: {validated_output.conclusion}"
