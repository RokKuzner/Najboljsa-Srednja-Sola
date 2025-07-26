from textblob import TextBlob
from deep_translator import GoogleTranslator

translator = GoogleTranslator(source='sl', target='en')

def determine_polarity(text:str) -> float:
    polarity:float = TextBlob(text).sentiment.polarity  # type: ignore
    return polarity

def translate(text:str):
    return translator.translate(text)