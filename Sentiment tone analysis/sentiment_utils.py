from textblob import TextBlob
import json
from google.cloud import translate_v2
import os
from dotenv import load_dotenv

load_dotenv()

def determine_polarity(text:str) -> float:
    polarity:float = TextBlob(text).sentiment.polarity  # type: ignore
    return polarity

def translate(text: str):
    if not os.environ.get('GOOGLE_APPLICATION_CREDENTIALS'):
        print("GOOGLE_APPLICATION_CREDENTIALS environment variable is not set")
        return ""
    
    translate_client = translate_v2.Client(target_language="en")

    try:
        result = translate_client.translate(text, target_language="en")
        translated_text = result["translatedText"]

        return translated_text
    except Exception as e:
        print(f"An error occurred during translation: {e}")
        return ""
