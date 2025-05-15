import os
import sys
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app.services.fetcher import fetch_news


@pytest.mark.asyncio
@patch(
    "app.services.fetcher.settings.news_api_url", "https://mockapi.com/news"
) 
@patch("httpx.AsyncClient.get", new_callable=AsyncMock)  
async def test_fetch_news(mock_get):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.raise_for_status = MagicMock()
    mock_response.json = AsyncMock(
        return_value={
            "articles": [
                {
                    "title": "Test Title",
                    "description": "Test Description",
                    "url": "http://example.com",
                }
            ]
        }
    )
    mock_get.return_value = mock_response

    data = await fetch_news("ai")
    assert isinstance(data, list)
    assert "title" in data[0]


@pytest.mark.asyncio
@patch("app.services.fetcher.settings.news_api_url", "https://mockapi.com/news")
@patch("httpx.AsyncClient.get", new_callable=AsyncMock)
async def test_sentiment_added(mock_get):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.raise_for_status = MagicMock()
    mock_response.json = AsyncMock(
        return_value={
            "articles": [
                {
                    "title": "Neutral News",
                    "description": "Just an update.",
                    "url": "http://example.com",
                }
            ]
        }
    )
    mock_get.return_value = mock_response

    data = await fetch_news("update")
    assert isinstance(data, list)
    assert "sentiment" in data[0]
