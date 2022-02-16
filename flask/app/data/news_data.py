from datetime import datetime, timedelta
from dotenv import load_dotenv
import requests
import os


load_dotenv()

URL = "https://newsapi.org/v2/everything?"
key = os.environ.get("newsApiKey")


def fetch_news(symbol:str, company:str) -> list:
    """Usa a API News para buscar notícias
    usando o simbolo e o nome da companhia
    como parametros de busca. Retorna as
    noticias em forma de dicionarios dentro
    de uma lista"""

    last_week = datetime.now() - timedelta(7)
    last_week = last_week.strftime("%Y-%m-%d")
    today = datetime.now().strftime("%Y-%m-%d")

    params = {
        "q": company,
        "qlnTitle": company,
        "apiKey": key,
        "from": last_week,
        "to": today,
        "language": "en",
        "sortBy": "popularity",
        "pageSize": "10"
    }

    response = requests.get(URL, params=params)
    response.raise_for_status()
    data = response.json()
    articles = data["articles"]

    # Cria uma lista de dicionários
    # contendo os dados das notícias
    news_list = []
    for article in articles:
        news = {
            "title": article["title"],
            "description": article["description"],
            "news_url": article["url"],
        }
        news_list.append(news)

    return news_list
