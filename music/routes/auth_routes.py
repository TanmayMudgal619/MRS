from flask_smorest import Blueprint
from flask.views import MethodView
from flask import render_template, Response
from controllers.auth_controller import AuthController
from helpers.token_validator import token_validator
from schemas import ResgisterSchema, SignInSchema

blp = Blueprint("Auth", __name__)


@blp.route("/sign-in")
class SignInRoute(MethodView):

    @token_validator
    def get(self):
        return render_template('sign_in.html')

    @token_validator
    @blp.arguments(SignInSchema)
    def post(self, json_body):
        return AuthController().sign_in(json_body)


@blp.route("/sign-up")
class SignUpRoute(MethodView):

    @token_validator
    def get(self):
        return render_template('sign_up.html')

    @token_validator
    @blp.arguments(ResgisterSchema)
    def post(self, json_body):
        return AuthController().sign_up(json_body)
