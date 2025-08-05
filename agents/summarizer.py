from tools.summarization_tool import LocalSummarizationTool


class NewsSummarizerAgent:
    def __init__(self):
        # Future: Load real summarization model
        self.summarizer = LocalSummarizationTool()
        pass

    def summarize_news(self, article_text: str) -> str:
        return self.summarizer.summarize(article_text)
