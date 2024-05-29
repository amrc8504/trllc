from flask import Flask, url_for, send_from_directory

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = "#"

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app
