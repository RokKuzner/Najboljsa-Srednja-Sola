from sentiment_utils import determine_polarity, translate
import json

# Get school data
with open("schools.json", "r") as f:
    schools = json.load(f)
