from src.beautifulsoup_request import getNewsData
from src.googlesearch_gnews import with_gnews, with_google_news_feed
import pandas as pd

def save_dataframe(news):
    df = pd.DataFrame(news)
    df.to_csv('news.csv', index=False)

query = "SENAI PB"

# news = getNewsData(query, 50)

# news = with_gnews(query)

news = with_google_news_feed(query)

save_dataframe(news)