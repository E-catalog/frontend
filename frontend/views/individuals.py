from http import HTTPStatus
from typing import Any

from flask import Blueprint, abort, redirect, render_template, request, url_for
from pydantic import ValidationError

from frontend.api.client import Client
from frontend.api.schemas import Individual
from frontend.config import config

routes = Blueprint('individuals', __name__)
client = Client(config.api_url)


@routes.get('/')
def render_individuals_page():
    individuals = client.individuals.get_all()
    places = client.places.get_all()
    return render_template(
        'individuals/all_individuals.html',
        individuals=[item.dict() for item in individuals],
        places=[item.dict() for item in places],
    )


@routes.post('/get/')
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


@routes.post('/create/')
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
    return redirect(url_for('individuals.render_individuals_page'))


@routes.post('/update/')
def update_individual():
    form_data: dict[str, Any] = request.form.to_dict()
    if not form_data:
        abort(HTTPStatus.BAD_REQUEST, 'Отсутствуют данные')

    try:
        payload = Individual(**form_data)
    except ValidationError:
        abort(HTTPStatus.BAD_REQUEST, 'Неверный тип данных в запросе')

    client.individuals.update(uid=form_data['uid'], payload=payload)
    return redirect(url_for('individuals.render_individuals_page'))


@routes.post('/delete/')
def delete_individual():
    form_data: dict[str, Any] = request.form.to_dict()
    if not form_data:
        abort(HTTPStatus.BAD_REQUEST, 'Отсутствуют данные')

    uid = form_data['uid']
    client.individuals.delete(uid)
    return redirect(url_for('individuals.render_individuals_page'))
