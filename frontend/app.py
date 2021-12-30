from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/')
def show_individuals():
    title = "Электронный каталог хранения"
    response = requests.get('http://192.168.1.64:5000/api/v1/individuals/')
    response.raise_for_status()
    individuals = response.json()
    return render_template('individuals.html', title=title, individuals=individuals)
