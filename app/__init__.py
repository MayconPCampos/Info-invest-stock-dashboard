from flask import Flask
from flask_caching import Cache


app = Flask(__name__)

from app import views