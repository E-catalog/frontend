from http import HTTPStatus
from typing import Any

from flask import Flask, abort, redirect, render_template, request, url_for
from pydantic import ValidationError

from frontend.api.client import Client
from frontend.api.models import Individual
from frontend.config import config

app = Flask(__name__)

client = Client(config.api_url)


@app.route('/')
def show_individuals(individual=None):
    title = 'Электронный каталог хранения'
    individuals = client.individuals.get_all()
    return render_template(
        'individuals.html',
        title=title,
        individuals=[item.dict() for item in individuals],
        individual=individual,
    )


@app.route('/individual')
def get_individual():
    form_data: dict[str, Any] = request.args
    if not form_data:
        abort(HTTPStatus.BAD_REQUEST, 'Отсутствуют данные')

    id_from_form = form_data['id']
    individual = client.individuals.get(id_from_form)
    return show_individuals(individual.dict())


@app.route('/', methods=['POST'])
def add_individual():
    form_data: dict[str, Any] = request.form.to_dict()
    if not form_data:
        abort(HTTPStatus.BAD_REQUEST, 'Отсутствуют данные')

    form_data['id'] = -1

    try:
        payload = Individual(**form_data)
    except ValidationError:
        abort(HTTPStatus.BAD_REQUEST, 'Неверный тип данных в запросе')

    client.individuals.add(payload)
    return redirect(url_for('show_individuals'))


@app.route('/individuals', methods=['POST'])
def update_individual():
    form_data: dict[str, Any] = request.form.to_dict()
    if not form_data:
        abort(HTTPStatus.BAD_REQUEST, 'Отсутствуют данные')

    try:
        payload = Individual(**form_data)
    except ValidationError:
        abort(HTTPStatus.BAD_REQUEST, 'Неверный тип данных в запросе')

    client.individuals.update(uid=form_data['id'], payload=payload)
    return redirect(url_for('show_individuals'))
