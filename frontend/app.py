from flask import Flask, render_template
import requests
import frontend.config as config


app = Flask(__name__)


@app.route('/')
def show_individuals():
    title = "Электронный каталог хранения"
    response = requests.get(config.API_URL)
    response.raise_for_status()
    individuals = response.json()
    return render_template('individuals.html', title=title, individuals=individuals)
