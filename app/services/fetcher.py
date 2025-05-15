import httpx
from app.core.config import settings
from app.services.sentiment import get_sentiment

async def fetch_news(topic: str = "technology", page: int = 1):
    params = {
        "q": topic,
        "apiKey": settings.news_api_key,
        "language": "en",
        "pageSize": 10,
        "page": page
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(settings.news_api_url, params=params)
        response.raise_for_status()
        json_data = await response.json()
        articles = json_data.get("articles", [])

        # Add sentiment analysis to each article
        for article in articles:
            content = article.get("description") or article.get("content") or ""
            article["sentiment"] = get_sentiment(content)

        return articles
