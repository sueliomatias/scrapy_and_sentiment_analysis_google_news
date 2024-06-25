import requests
import json
from bs4 import BeautifulSoup

def getNewsData(search):
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
    }
    response = requests.get(f"https://www.google.com/search?q={search}&gl=pt&tbm=nws&num=5", headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    news_results = []

    for el in soup.select("div.SoaBEf"):
        news_results.append({
            "link": el.find("a")["href"],
            "title": el.select_one("div.n0jPhd").get_text(),
            "snippet": el.select_one(".GI74Re").get_text(),
            "date": el.select_one(".OSrXXb span").get_text(),
            "source": el.select_one(".NUnG9d span").get_text()
        })
        # print(json.dumps(news_results, indent=2))
    return news_results


