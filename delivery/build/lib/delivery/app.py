from flask import Flask

def create_app():
    app = Flask(__name__)#__name__ mesma coisa que delivery/app.py(por convensao usa __name)
    return app
