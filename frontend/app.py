import logging
from http import HTTPStatus

from flask import abort, Flask, redirect, render_template, request, url_for
from pydantic import ValidationError

from frontend.api.client import Client
from frontend.api.models import Individual
from frontend.config import config

app = Flask(__name__)

client = Client(config.api_url)
logger = logging.getLogger(__name__)


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
    form_data = request.json
    if not form_data:
        abort(HTTPStatus.BAD_REQUEST, 'Тело запроса не может быть пустым')

    form_data['uid'] = -1

    try:
        payload = Individual(**form_data)
    except ValidationError as error:
        logger.info('Ошибка в процессе pydantic-валидации: %s', error)
        abort(HTTPStatus.BAD_REQUEST, 'Неверный тип данных в запросе')

    client.individuals.add(payload)
    return redirect(url_for('show_individuals'))
