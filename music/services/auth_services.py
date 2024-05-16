from uuid import uuid4
from pymysql import IntegrityError
from database.mysql_access import MysqlAccess
from helpers.constants import SqlQueries
from flask import make_response

class AuthServices:
    def sign_in(self, email, password):
        with MysqlAccess() as cursor:
            cursor.execute(SqlQueries.SIGN_IN, (email,))
            user_data = cursor.fetchone()

            if not user_data:
                return {
                    "error_code": 401,
                    "error_status": "un-authorized",
                    "error_message": "username do not exists in database!"
                }, 401

            if user_data["hash_password"] != password:
                return {
                    "error_code": 401,
                    "error_status": "un-authorized",
                    "error_message": "password do not match!"
                }, 401

            response = make_response({"result": "success"})
            response.set_cookie("jwt", str(user_data["id"]))
            return response

    def sign_up(self, email, username, password):
        with MysqlAccess() as cursor:
            user_id = uuid4()
            try:
                cursor.execute(SqlQueries.SIGN_UP, (str(user_id)[:10], email, username, password))
            except IntegrityError:
                return {
                    "error_code": 409,
                    "error_status": "conflict",
                    "error_message": "username already in use!"
                }, 409
            return {
                "result": "created",
                "ref": user_id
            }
