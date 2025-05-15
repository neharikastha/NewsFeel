# 📰 News Aggregator (FastAPI + Sentiment Analysis )

A lightweight news aggregator built with **FastAPI**, that fetches news by topic, performs sentiment analysis, and displays articles with optional filtering.

---

##  Features

- Search news by topic (e.g., technology, business, sports)
- Sentiment analysis 
- Filter to show only **positive** news
- Responsive UI using simple HTML & CSS
- Containerized with Docker + CI/CD using GitHub Actions
- Uses 12 factor principles

---

##  Tech Stack

- FastAPI
- Jinja2 (template rendering)
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
source fastapi/bin/activate  # or fastapi\Scripts\activate on Windows

# Install requirements
pip install -r requirements.txt
