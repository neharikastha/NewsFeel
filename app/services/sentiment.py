from transformers import pipeline

# Load the sentiment pipeline once
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def get_sentiment(text: str) -> str:
    if not text.strip():
        return "Unknown"

    # Run sentiment analysis on the first 512 characters
    result = sentiment_pipeline(text[:512])[0]
    label = result["label"]  # 'POSITIVE' or 'NEGATIVE'
    return label.capitalize()
