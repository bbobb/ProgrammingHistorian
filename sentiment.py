from textblob import TextBlob

# Load text
with open("freud.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Split by paragraph
paragraphs = text.split('\n\n')

# Analyze
results = []
for i, para in enumerate(paragraphs):
    blob = TextBlob(para)
    polarity = blob.sentiment.polarity
    results.append((i, polarity))

# Save/write output
with open("sentiment_scores.csv", "w") as f:
    f.write("Paragraph,Polarity\n")
    for i, p in results:
        f.write(f"{i},{p}\n")

