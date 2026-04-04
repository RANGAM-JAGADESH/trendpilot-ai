import requests
from bs4 import BeautifulSoup
from trends.models import Trend


def fetch_google_news_trends():
    url = "https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    articles = soup.select("article h3")

    trends_added = 0

    for article in articles[:15]:
        title = article.text.strip()

        # Avoid duplicates
        if not Trend.objects.filter(title=title).exists():
            Trend.objects.create(
                title=title,
                source="Google News"
            )
            trends_added += 1

    return f"{trends_added} trends added"