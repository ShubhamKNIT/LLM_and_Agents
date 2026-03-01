import spacy
from nltk.tokenize import RegexpTokenizer

# Spacy offers simple tokenization using the nlp object, which can be used to tokenize text into words, sentences, etc.
# NLTK offerrs various tokenizers, including StringTokenizer, WordPunctTokenizer, RegexpTokenizer, etc.

class Tokenizer:
    def __init__(self, tokenizer_type: str = "spacy"):
        self.tokenizer_type = tokenizer_type
        if tokenizer_type == "spacy":
            self.nlp = spacy.load("en_core_web_sm")
        elif tokenizer_type == "nltk":
            self.tokenizer = RegexpTokenizer(r'\w+')
        else:
            raise ValueError("Unsupported tokenizer type. Use 'spacy' or 'nltk'.")
    
    def spacy_tokenize(self, text):
        doc = self.nlp(text)
        return [token.text for token in doc]

    def nltk_tokenize(self, text):
        return self.tokenizer.tokenize(text)

    def tokenize(self, text):
        if self.tokenizer_type == "spacy":
            return self.spacy_tokenize(text)
        elif self.tokenizer_type == "nltk":
            return self.nltk_tokenize(text)
        else:
            raise ValueError("Unsupported tokenizer type. Use 'spacy' or 'nltk'.")
