from textblob import TextBlob

def determine_polarity(text:str) -> float:
    polarity:float = TextBlob(text).sentiment.polarity 
    return polarity
