import requests
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/', methods=['GET', 'POST'])
def index():
    url = "https://ip-geolocation-ipwhois-io.p.rapidapi.com/json/"
    api_key = "45c974ed84mshc94c890bbd503ffp1d0eb4jsn218473e78459""
