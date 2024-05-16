import os
import dotenv
import openai

from flask_jwt_extended import JWTManager


dotenv.load_dotenv()

def config(app):
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
    openai.api_key = os.environ.get("OPEN_API_KEY")


def register_jwt(app):
    jwt = JWTManager(app)
