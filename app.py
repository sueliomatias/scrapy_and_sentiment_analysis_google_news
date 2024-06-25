from src.beautifulsoup_request import getNewsData
from src.googlesearch_gnews import with_gnews
import pandas as pd

def save_dataframe(news):
    df = pd.DataFrame(news)
    df.to_csv('news.csv', index=False)

news = getNewsData("SENAI PB")
save_dataframe(news)