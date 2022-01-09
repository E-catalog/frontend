from flask import Flask, render_template, request

from frontend.api.client import Client
from frontend.config import config

app = Flask(__name__)

client = Client(config.api_url)


@app.route('/')
def show_individuals():
    title = 'Электронный каталог хранения'
    individuals = client.individuals.get_all()
    return render_template(
        'individuals.html',
        title=title,
        individuals=[item.dict() for item in individuals],
    )


@app.route('/', methods=['POST'])
def add_individual():
    return request.form
