# 📰 News Feel (FastAPI + Sentiment Analysis)

A news aggregator built with **FastAPI**, that fetches news by topic, performs sentiment analysis, and displays positive articles by filtering.

---

## Features

- Search news by topic (e.g., technology, business, sports, AI, entertainment) and navigates to  the webpage for full length news
- Sentiment analysis using `distilbert-base-uncased-finetuned-sst-2-english`
- Filter to show only **positive** news
- Responsive UI using simple HTML & CSS 
- Containerized with Docker + CI/CD using GitHub Actions
- Uses 12 factor app principles

---

##  Tech Stack

- FastAPI
- Jinja2 
- Transformers (`huggingface/transformers`)
- httpx (async HTTP requests)
- Docker 
- GitHub Actions for CI

---

##  Setup

```bash
# Clone and enter
git clone https://github.com/neharikastha/NewsFeel.git
cd NewsFeel

# Set up virtual environment
python -m venv fastapi
fastapi\Scripts\activate on Windows

# Install requirements
pip install -r requirements.txt
```
---

## Set .env
```bash
NEWS_API_KEY=your_newsapi_key
NEWS_API_URL=your_newsapi_url
```
---

## Run the app
```bash
uvicorn app.main:app --reload
```
---

## Run with Docker
```bash
docker build -t newsfeel .
docker run -p 8000:8000 newsfeel



