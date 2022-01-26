from flask import Flask, render_template

from frontend.views import individuals, places


def create_app():
    app = Flask(__name__, static_url_path='/static')

    @app.route('/')
    def render_main_page():
        return render_template('main_page.html')

    app.register_blueprint(individuals.routes, url_prefix='/individuals')
    app.register_blueprint(places.routes, url_prefix='/places')

    return app


app = create_app()
