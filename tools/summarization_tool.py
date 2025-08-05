from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer


class LocalSummarizationTool:
    def __init__(self):
        self.summarizer = LsaSummarizer()

    def summarize(self, text: str, sentence_count: int = 3) -> str:
        if not text or len(text.strip()) < 30:
            return "⚠️ Please provide a longer article or paragraph."

        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        summary_sentences = self.summarizer(parser.document, sentence_count)

        bullets = [f"• {sentence}" for sentence in summary_sentences]
        return "\n".join(bullets)
