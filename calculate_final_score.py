import json

# Get school data
with open("schools.json", "r") as f:
    schools = json.load(f)

# Get the maximum amount of posts per school
max_posts_per_school = 0
for school in schools:
    if len(school["articles"]) > max_posts_per_school:
        max_posts_per_school = len(school["articles"])

# Calculate score for each school and keep track of the best school so far
best_school = {}
best_school_score = 0

for i, school in enumerate(schools):
    score = school["matura_score"] * (1/2) + (school["sentiment_score"]+1) * 50 * (3/10) + len(school["articles"])/max_posts_per_school * 20

    school["score"] = score
    schools[i] = school
    
    if score > best_school_score:
        best_school_score = score
        best_school = school

# Save data
with open("schools.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(schools, ensure_ascii=False))

print(f"The best school in SLO is ..... {best_school["name"]} with {best_school_score} points.")