from marshmallow import Schema
from marshmallow.fields import String


class ResgisterSchema(Schema):
    email = String(required=True)
    password = String(required=True)
    username = String(required=True)


class SignInSchema(Schema):
    email = String(required=True)
    password = String(required=True)
