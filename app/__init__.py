from flask import Flask
from flask_caching import Cache

config = {"CACHE_TYPE": "SimpleCache"}

app = Flask(__name__)
app.config.from_mapping(config)

cache = Cache(app)

from app import views