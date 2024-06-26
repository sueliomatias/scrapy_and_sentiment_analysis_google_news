from googlesearch import search
from gnews import GNews
import feedparser
import pandas as pd

def with_google_search(query):
    search_results = search(query, num_results=10, lang='pt-BR', advanced=True, extra_params={"filter": "0"})

    for url in search_results:
        print(url)

def with_gnews(query):
    google_news = GNews(language='pt', country='BR', max_results=100, period='7d')
    news = google_news.get_news(query)
    return news

def with_google_news_feed(query):
    query = "%20".join(query.split(" "))
    rss_url = f"https://news.google.com/rss/search?q={query}&hl=pt-BR&gl=BR&ceid=BR:pt-419"
    feed = feedparser.parse(rss_url)
    data = []
    if feed.entries:
        for entry in feed.entries:
            title = entry.title
            link = entry.link
            description = entry.description
            pubdate = entry.published
            source_title = entry.source.title
            source_link = entry.source.href
            data.append({
                "title": title,
                "link": link,
                "description": description,
                "pubdate": pubdate,
                "source_title": source_title,
                "source_link": source_link
            })
    else:
        print("Nenhum resultado encontrado.")
        
    return data