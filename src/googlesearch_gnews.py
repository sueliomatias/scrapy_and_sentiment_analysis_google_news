from googlesearch import search
from gnews import GNews

def with_google_search(query):
    search_results = search(query, num_results=10, lang='pt-BR', advanced=True, extra_params={"filter": "0"})

    for url in search_results:
        print(url)

def with_gnews(query):
    google_news = GNews()
    news = google_news.get_news(query)
    return news
