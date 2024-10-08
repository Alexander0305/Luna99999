import rasa
import nltk
from nltk.tokenize import word_tokenize

class NLP:
    def __init__(self, model, language):
        self.model = model
        self.language = language
        self.nlp = rasa.NLP(model, language)
        nltk.download('punkt')

    def process_text(self, text):
        tokens = word_tokenize(text)
        return self.nlp.process(text)

    def get_intent(self, text):
        response = self.process_text(text)
        return response.intent

    def get_entities(self, text):
        response = self.process_text(text)
        return response.entities
