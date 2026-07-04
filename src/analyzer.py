
from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)

    polarity = blob.sentiment.polarity
    if polarity > 0:
        sentiment_label = "positive"
    elif polarity < 0:
        sentiment_label = "negative"
    else:
        sentiment_label = "neutral"
    return sentiment_label, round(polarity, 2)


