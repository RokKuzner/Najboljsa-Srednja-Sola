from textblob import TextBlob
from deep_translator import GoogleTranslator
import time

def determine_polarity(text:str) -> float:
    polarity:float = TextBlob(text).sentiment.polarity  # type: ignore
    return polarity

def translate_with_google_unofficial(text):
    try:
        translator = GoogleTranslator(source='sl', target='en')

        chunk_size = 4500
        translated_chunks = []
        for i in range(0, len(text), chunk_size):
            chunk = text[i:i + chunk_size]
            translated_chunks.append(translator.translate(chunk))
            time.sleep(0.2)
        
        return "".join(translated_chunks)
    
    except Exception as e:
        print(f"Error with unofficial Google Translator: {e}")
        return ""