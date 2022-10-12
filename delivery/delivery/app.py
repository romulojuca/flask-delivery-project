from flask import Flask
from delivery.ext import config


def create_app():
    app = Flask(__name__)#__name__ mesma coisa que delivery/app.py(por convensao usa __name)
    config.init_app(app)

    return app
