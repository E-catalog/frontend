from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
#def hello():
#    page_title = "Электронный каталог хранения"
#    return render_template('hello.html', title=page_title)


#@app.route('/api/v1/individuals/')
def show_individuals():
    response = requests.get('http://localhost:5000/api/v1/individuals/')
    response.raise_for_status()
    individuals = response.json
    return render_template('individuals.html', individuals=individuals)
