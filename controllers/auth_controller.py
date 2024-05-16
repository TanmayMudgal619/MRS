from services.auth_services import AuthServices


class AuthController:
    def sign_in(self, json_data):
        email = json_data["email"]
        password = json_data["password"]

        return AuthServices().sign_in(email, password)

    def sign_up(self, json_data):
        email = json_data["email"]
        username = json_data["username"]
        password = json_data["password"]

        return AuthServices().sign_up(email, username, password)
