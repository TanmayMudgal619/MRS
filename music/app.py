from flask import Flask
from routes import register_blueprints
from config import config, register_jwt

def create_app():
    app = Flask(__name__)

    config(app)
    register_jwt(app)
    register_blueprints(app)

    return app


app = create_app()