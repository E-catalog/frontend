from http import HTTPStatus

from flask import Flask, abort, redirect, render_template, request, url_for
from pydantic import ValidationError

from frontend.api.client import Client
from frontend.api.models import Individual
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
    form_data = request.form.to_dict()
    if not form_data:
        abort(HTTPStatus.BAD_REQUEST, 'Отсутствуют данные')

    form_data['id'] = '-1'

    try:
        payload = Individual(**form_data)
    except ValidationError:
        abort(HTTPStatus.BAD_REQUEST, 'Неверный тип данных в запросе')

    client.individuals.add(payload)
    return redirect(url_for('show_individuals'))
