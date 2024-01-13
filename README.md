# Stock Dashboard

Displays the values of the last seven days of a stock and calculates the value and percentage of variation, typically used for evaluating the performance of a stock. It also shows company information and recent related news obtained through the News API.

Due to the request limit of the plan used for the Alpha Vantage API, I have limited it to only show stocks of one company. However, it can easily be modified to show other stocks by changing the route code in the views.py file as shown below.

```

@app.route("/stocks/<id>")
@cache.cached(timeout=60)
def stock(id):

    id = id

```


This mini app was created using my Docker-Flask image <a href="https://github.com/MayconPCampos/Ambiente-docker-flask"> link here</a>.

To run it, clone this repository using the command git clone https://github.com/MayconPCampos/Mini-dashboard.git in Git Bash. If you have Docker installed, simply run the command docker-compose up in the console inside the repository directory. If you don't have Docker installed, install the dependencies with the command pip install -r requirements.txt inside the app directory, then start it with flask run. You need to create an .env file in the directory with the keys for accessing both APIs.

Access it through the URL localhost:5000/stocks/TSLA.
