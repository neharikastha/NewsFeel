from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.services.fetcher import fetch_news

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def read_news(request: Request, topic: str = "technology", page: int = 1, positive_only: bool = False):
    articles = await fetch_news(topic, page)
    if positive_only:
        articles = [a for a in articles if a.get("sentiment") == "Positive"]
    return templates.TemplateResponse("index.html", {
        "request": request,
        "articles": articles,
        "topic": topic,
        "page": page,
        "positive_only": positive_only,

    })
