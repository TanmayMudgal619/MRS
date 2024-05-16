from flask import request, redirect


def token_validator(func):
    def validate_token(*args, **kwargs):
        jwt_cookie = request.cookies.get("jwt")
        if jwt_cookie:
            return redirect("/")
        return func(*args, **kwargs)
    return validate_token


def not_signed_in(func):
    def validate_token(*args, **kwargs):
        jwt_cookie = request.cookies.get("jwt")
        if not jwt_cookie:
            return redirect("/sign-in")
        return func(*args, **kwargs)
    return validate_token