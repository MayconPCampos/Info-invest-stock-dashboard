from dotenv import load_dotenv
import os
import requests


load_dotenv()

URL = "https://www.alphavantage.co/query?"
key = os.environ.get("alphaVantageKey")


def fetch_company(id:str) -> dict:
    """Faz a requisição dos dados da companhia
    e retorna em forma de dicionário"""

    parameters = {
        "function": "OVERVIEW",
        "symbol": id,
        "apikey": key
    }

    response = requests.get(URL, params=parameters)
    response.raise_for_status()
    data = response.json()

    return data


def fetch_stock(id:str) -> list:
    """Usa a API da Alpha Vantage para realizar
    a busca do historico de preços das ações da
    companhia usando o seu respectivo simbolo na
    bolsa, cria um dicionário para cada dado e os
    retorna dentro de uma lista"""

    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": id,
        "apikey": key
    }

    response = requests.get(URL, params=parameters)
    response.raise_for_status()
    stock_data = response.json()

    # Selecionando apenas dados necessários
    data = stock_data["Time Series (Daily)"]

    stock_list = []
    for stock in data:
        new = {
        "date": stock,
        "low": data[stock]["3. low"],
        "open": float(data[stock]["1. open"]),
        "high": float(data[stock]["2. high"]),
        "close": float(data[stock]["4. close"]),
        "volume": int(data[stock]["5. volume"])
        }
        stock_list.append(new)

    return stock_list
