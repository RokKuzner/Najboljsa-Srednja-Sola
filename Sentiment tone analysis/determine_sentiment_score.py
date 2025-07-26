from sentiment_utils import determine_polarity, translate
import json

# Get school data
with open("schools.json", "r") as f:
    schools = json.load(f)

# Calculate scores
for indx, school in enumerate(schools):
    scores:list[float] = []

    for article in school["articles"]:
        scores.append( determine_polarity( translate( article) ) )

    score = sum(scores) / len(scores)

    # Save score
    schools[indx]["sentiment_score"] = score