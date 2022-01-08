import requests
from flask import Flask, render_template, request

from frontend.config import config

app = Flask(__name__)


@app.route('/')
def show_individuals():
    title = 'Электронный каталог хранения'
    url = f'{config.api_url}/api/v1/individuals/'
    response = requests.get(url)
    response.raise_for_status()
    individuals = response.json()
    return render_template('individuals.html', title=title, individuals=individuals)


@app.route('/', methods=['POST'])
def add_individual():
    return request.form
