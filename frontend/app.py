from http import HTTPStatus
from typing import Any

from flask import Flask, abort, redirect, render_template, request, url_for
from pydantic import ValidationError

from frontend.api.client import Client
from frontend.api.models import Individual, Place
from frontend.config import config

app = Flask(__name__, static_url_path='/static')

client = Client(config.api_url)


@app.route('/')
def show_individuals():
    title = 'Электронный каталог хранения'
    individuals = client.individuals.get_all()
    return render_template(
        'main_page.html',
        title=title,
        individuals=[item.dict() for item in individuals],
    )


@app.route('/individuals/get/', methods=['POST'])
def get_individual():
    form_data: dict[str, Any] = request.form.to_dict()
    if not form_data:
        abort(HTTPStatus.BAD_REQUEST, 'Отсутствуют данные')

    id_from_form = form_data['id']
    individual = client.individuals.get(id_from_form)
    return render_template('individuals/update_individual_form.html', individual=individual.dict())


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

    id_from_form = form_data['id']
    client.individuals.delete(id_from_form)
    return show_individuals()




@app.route('/places/get/', methods=['POST'])
def get_place():
    form_data: dict[str, Any] = request.form.to_dict()
    if not form_data:
        abort(HTTPStatus.BAD_REQUEST, 'Отсутствуют данные')

    id_from_form = form_data['id']
    place = client.place.get(id_from_form)
    return render_template('places/update_places_form.html', place=place.dict())



@app.route('/places/update/', methods=['POST'])
def update_place():
    form_data: dict[str, Any] = request.form.to_dict()

    if not form_data:
        abort(HTTPStatus.BAD_REQUEST, 'Отсутствуют данные')

    try:
        payload = Place(**form_data)
    except ValidationError:
        abort(HTTPStatus.BAD_REQUEST, 'Неверный тип данных в запросе')

    client.places.update(uid=form_data['uid'], payload=payload)
    return redirect(url_for('show_places'))


@app.route('/places/create/', methods=['POST'])
def add_place():
    form_data: dict[str, Any] = request.form.to_dict()
    if not form_data:
        abort(HTTPStatus.BAD_REQUEST, 'Отсутствуют данные')

    form_data['uid'] = -1

    try:
        payload = Place(**form_data)
    except ValidationError:
        abort(HTTPStatus.BAD_REQUEST, 'Неверный тип данных в запросе')

    client.places.add(payload)
    return redirect(url_for('show_individuals'))

@app.route('/places/delete/', methods=['POST'])
def delete_place():
    form_data: dict[str, Any] = request.form.to_dict()
    if not form_data:
        abort(HTTPStatus.BAD_REQUEST, 'Отсутствуют данные')

    id_from_form = form_data['id']
    client.places.delete(id_from_form)
    return redirect(url_for('show_places'))

