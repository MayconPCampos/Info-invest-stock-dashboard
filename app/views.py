from app.stock_data import fetch_stock, fetch_company
from flask import render_template
from app.stock import Stock
from app import app, news_data


@app.route("/stocks/TSLA")
def stock():

    id = "TSLA"
    stock_list = fetch_stock(id)
    stock = Stock(stock_list)

    # valor da variação
    change = stock.get_change()

    # informações sobre a companhia
    company = fetch_company(id)
    company_name = company.get("Name")
    news_list = news_data.fetch_news(id, company_name)

    return render_template(
        "stock.html",
        change=change,
        company=company,
        stock=stock,
        news_list=news_list
    )
