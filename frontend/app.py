from http import HTTPStatus
from typing import Any

from flask import Flask, abort, redirect, render_template, request, url_for
from pydantic import ValidationError

from frontend.api.client import Client
from frontend.api.schemas import Individual, Place
from frontend.config import config

app = Flask(__name__, static_url_path='/static')

client = Client(config.api_url)


@app.route('/')
def render_main_page():
    return render_template('main_page.html')


@app.route('/individuals')
def render_individuals_page():
    individuals = client.individuals.get_all()
    places = client.places.get_all()
    return render_template(
        'individuals/all_individuals.html',
        individuals=[item.dict() for item in individuals],
        places=[item.dict() for item in places],
    )


@app.route('/places')
def render_places_page():
    places = client.places.get_all()
    return render_template(
        'places/all_places.html',
        places=[item.dict() for item in places],
    )


@app.route('/individuals/get/', methods=['POST'])
def get_individual():
    form_data: dict[str, Any] = request.form.to_dict()
    if not form_data:
        abort(HTTPStatus.BAD_REQUEST, 'Отсутствуют данные')

    uid = form_data['uid']
    individual = client.individuals.get(uid)
    places = client.places.get_all()
    return render_template(
        'individuals/update_individual_form.html',
        individual=individual.dict(),
        places=places,
    )


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
    return redirect(url_for('render_individuals_page'))


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
    return redirect(url_for('render_individuals_page'))


@app.route('/individuals/delete/', methods=['POST'])
def delete_individual():
    form_data: dict[str, Any] = request.form.to_dict()
    if not form_data:
        abort(HTTPStatus.BAD_REQUEST, 'Отсутствуют данные')

    uid = form_data['uid']
    client.individuals.delete(uid)
    return redirect(url_for('render_individuals_page'))


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
    return redirect(url_for('render_places_page'))


@app.route('/places/get/', methods=['POST'])
def get_place():
    form_data: dict[str, Any] = request.form.to_dict()
    if not form_data:
        abort(HTTPStatus.BAD_REQUEST, 'Отсутствуют данные')

    uid = form_data['uid']
    place = client.places.get(uid)
    return render_template('places/update_place_form.html', place=place.dict())


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
    return redirect(url_for('render_places_page'))


@app.route('/places/delete/', methods=['POST'])
def delete_place():
    form_data: dict[str, Any] = request.form.to_dict()
    if not form_data:
        abort(HTTPStatus.BAD_REQUEST, 'Отсутствуют данные')

    uid = form_data['uid']
    client.places.delete(uid)
    return redirect(url_for('render_places_page'))
