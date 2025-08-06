import logfire
from tools.summarization_tool import LocalSummarizationTool
from models.summarizer import SummarizerInput, SummarizerOutput


class NewsSummarizerAgent:
    def __init__(self):
        self.summarizer = LocalSummarizationTool()

    @logfire.instrument()
    def summarize_news(self, article_text: str) -> str:
        validated_input = SummarizerInput(article_text=article_text)
        logfire.info("Summarizing article", input_length=len(article_text))
        bullet_text = self.summarizer.summarize(validated_input.article_text)
        bullet_lines = [line.strip() for line in bullet_text.split("\n") if line.strip().startswith("•")]
        validated_output = SummarizerOutput(summary_bullets=bullet_lines)
        logfire.info("Summary completed", bullet_count=len(bullet_lines))
        return "\n".join(validated_output.summary_bullets)
