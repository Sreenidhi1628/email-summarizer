from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import nltk

nltk.download('punkt')
nltk.download('punkt_tab')

def summarize_email(email_text, length="Medium"):
    sentence_count = {
        "Short": 2,
        "Medium": 4,
        "Detailed": 7
    }

    parser = PlaintextParser.from_string(email_text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentence_count[length])

    return " ".join([str(sentence) for sentence in summary])