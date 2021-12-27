from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def hello():
    page_title = "Электронный каталог хранения"
    return render_template('hello.html', title=page_title)
