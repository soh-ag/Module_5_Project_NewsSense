import logfire
from tools.rag_tool import RAGTool
from models.fact_checker import FactCheckInput, FactCheckOutput
import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner
from schemas.fact_checker import FactCheckResult

# Optional: Load API key from environment (if needed)
# Load environment variables
load_dotenv()

BASE_URL = os.getenv("BASE_URL") 
API_KEY = os.getenv("API_KEY") 
MODEL_NAME = os.getenv("MODEL_NAME") 

# Initialize OpenAI async client
if not BASE_URL or not API_KEY or not MODEL_NAME:
    raise ValueError(
        "Please set BASE_URL, API_KEY, and MODEL_NAME."
    )
    

client = AsyncOpenAI(base_url=BASE_URL, api_key=API_KEY)


# Step 1: Define instruction to control GPT behavior
FACT_CHECKER_INSTRUCTIONS = """
You are an expert fact-checking AI assistant.
Given a claim, determine whether it is TRUE or FALSE.

Respond with structured JSON:
- claim: the input claim
- is_true: true or false
- explanation: a short paragraph explaining your reasoning
- sources: list of links or source names that support your conclusion

Be honest and objective.
"""

# Step 2: Create the agent with model, instruction, and output type
fact_checker_agent = Agent(
    name="Fact Checker AI",
    instructions=FACT_CHECKER_INSTRUCTIONS,
    model=OpenAIChatCompletionsModel(model=MODEL_NAME, openai_client=client),
    output_type=FactCheckResult
)

# Step 3: Async runner function to use the agent
async def run_fact_check(claim: str) -> FactCheckResult:
    result = await Runner.run(fact_checker_agent, claim)
    return result.final_output


class FactCheckerAgent:
    def __init__(self):
        self.rag_tool = RAGTool()

    @logfire.instrument()
    def verify_claim(self, claim: str) -> str:
        logfire.info("Verifying claim", claim=claim)
        validated_input = FactCheckInput(claim=claim)
        sources, conclusion = self.rag_tool.retrieve_sources(validated_input.claim)
        validated_output = FactCheckOutput(sources=sources, conclusion=conclusion)
        logfire.info("Fact check result", sources_found=len(sources), conclusion=conclusion)
        sources_text = "\n".join(f"🔗 {s}" for s in validated_output.sources)
        return f"{sources_text}\n\n🧾 Conclusion: {validated_output.conclusion}"
