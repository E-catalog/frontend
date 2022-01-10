from flask import Flask, redirect, render_template, request, url_for

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
    form_data = dict(request.form)
    client.individuals.add(form_data)
    return redirect(url_for('show_individuals'))
