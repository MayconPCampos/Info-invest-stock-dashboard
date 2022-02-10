from data.stock_data import fetch_stock, fetch_company
from data.news_data import fetch_news
from flask import render_template
from app.stock import Stock
from app import app, cache


@app.route("/stocks/TSLA")
@cache.cached(timeout=60)
def stock():

    id = "TSLA"
    stock_list = fetch_stock(id)
    stock = Stock(stock_list)

    # valor da variação
    change = stock.get_change()

    # informações sobre a companhia
    company = fetch_company(id)
    company_name = company.get("Name")

    # obtem noticias da companhia
    news_list = fetch_news(id, company_name)

    return render_template(
        "stock.html",
        change=change,
        company=company,
        stock=stock,
        news_list=news_list
    )
