from http import HTTPStatus
from typing import Any

from flask import Flask, abort, redirect, render_template, request, url_for
from pydantic import ValidationError

from frontend.api.client import Client
from frontend.api.models import Individual
from frontend.config import config

app = Flask(__name__, static_url_path='/static')

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


@app.route('/individuals/get/', methods=['POST'])
def get_individual():
    form_data: dict[str, Any] = request.form.to_dict()
    if not form_data:
        abort(HTTPStatus.BAD_REQUEST, 'Отсутствуют данные')

    id_from_form = form_data['uid']
    individual = client.individuals.get(id_from_form)
    return render_template('update_individual_form.html', individual=individual.dict())


@app.route('/individuals/create/', methods=['POST'])
def add_individual():
    form_data: dict[str, Any] = request.form.to_dict()
    if not form_data:
        abort(HTTPStatus.BAD_REQUEST, 'Отсутствуют данные')

    form_data['uid'] = -1

    try:
        payload = Individual(**form_data)
    except ValidationError:
        abort(HTTPStatus.BAD_REQUEST, 'Неверный тип данных в запросе')

    client.individuals.add(payload)
    return redirect(url_for('show_individuals'))


@app.route('/individuals/update/', methods=['POST'])
def update_individual():
    form_data: dict[str, Any] = request.form.to_dict()
    if not form_data:
        abort(HTTPStatus.BAD_REQUEST, 'Отсутствуют данные')

    try:
        payload = Individual(**form_data)
    except ValidationError:
        abort(HTTPStatus.BAD_REQUEST, 'Неверный тип данных в запросе')

    client.individuals.update(uid=form_data['uid'], payload=payload)
    return redirect(url_for('show_individuals'))


@app.route('/individuals/delete/', methods=['POST'])
def delete_individual():
    form_data: dict[str, Any] = request.form.to_dict()
    if not form_data:
        abort(HTTPStatus.BAD_REQUEST, 'Отсутствуют данные')

    id_from_form = form_data['uid']
    client.individuals.delete(id_from_form)
    return show_individuals()
