from sentiment_utils import determine_polarity, translate_with_google_unofficial
import json

# Get school data
with open("schools.json", "r") as f:
    schools = json.load(f)

# Calculate scores
try:
    for indx, school in enumerate(schools):
        scores:list[float] = []

        for article in school["articles"]:
            try:
                scores.append( determine_polarity( translate_with_google_unofficial( article ) ) )
            except Exception as e:
                print(f"Error when calculating sentiment scores: {e}")
                continue

        if len(scores) != 0:
            score = sum(scores) / len(scores)
        else:
            score = 0

        # Save score
        schools[indx]["sentiment_score"] = score
except Exception as e:
    print(f"Error when calculating sentiment scores - outside loop: {e}")
finally:
    # Save data
    with open("schools.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(schools, ensure_ascii=False))