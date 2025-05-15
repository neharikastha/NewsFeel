import pytest
import sys
import os
from unittest.mock import patch, AsyncMock, MagicMock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.services.fetcher import fetch_news

@pytest.mark.asyncio
@patch("httpx.AsyncClient.get", new_callable=AsyncMock)
async def test_fetch_news(mock_get):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.raise_for_status = MagicMock()
    mock_response.json = AsyncMock(return_value={
        "articles": [
            {
                "title": "Test Title",
                "description": "Test Description",
                "url": "http://example.com"
            }
        ]
    })
    mock_get.return_value = mock_response

    data = await fetch_news("ai")
    assert isinstance(data, list)
    assert "title" in data[0] 