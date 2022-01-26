from http import HTTPStatus
from typing import Any

from flask import Blueprint, abort, redirect, render_template, request, url_for
from pydantic import ValidationError

from frontend.api.client import Client
from frontend.api.schemas import Place
from frontend.config import config

routes = Blueprint('places', __name__)
client = Client(config.api_url)


@routes.get('/')
def render_places_page():
    places = client.places.get_all()
    return render_template(
        'places/all_places.html',
        places=[item.dict() for item in places],
    )


@routes.post('/get/')
def get_place():
    form_data: dict[str, Any] = request.form.to_dict()
    if not form_data:
        abort(HTTPStatus.BAD_REQUEST, 'Отсутствуют данные')

    uid = form_data['uid']
    place = client.places.get(uid)
    return render_template('places/update_place_form.html', place=place.dict())


@routes.post('/create/')
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
    return redirect(url_for('places.render_places_page'))


@routes.post('/update/')
def update_place():
    form_data: dict[str, Any] = request.form.to_dict()

    if not form_data:
        abort(HTTPStatus.BAD_REQUEST, 'Отсутствуют данные')

    try:
        payload = Place(**form_data)
    except ValidationError:
        abort(HTTPStatus.BAD_REQUEST, 'Неверный тип данных в запросе')

    client.places.update(uid=form_data['uid'], payload=payload)
    return redirect(url_for('places.render_places_page'))


@routes.post('/delete/')
def delete_place():
    form_data: dict[str, Any] = request.form.to_dict()
    if not form_data:
        abort(HTTPStatus.BAD_REQUEST, 'Отсутствуют данные')

    uid = form_data['uid']
    client.places.delete(uid)
    return redirect(url_for('places.render_places_page'))
