import os
import pymysql
from pymysql.cursors import DictCursor


class MysqlAccess:
    def __init__(self) -> None:
        self.__database = pymysql.connect(
            host="musicrecommendsys.mysql.pythonanywhere-services.com",
            database=os.environ.get("DATABASE_NAME"),
            user=os.environ.get("DATABASE_USER"),
            password=os.environ.get("DATABASE_PASSWORD")
        )

    def __enter__(self, cursor=DictCursor):
        self.__cursor = self.__database.cursor(cursor)
        return self.__cursor

    def __exit__(self, *errors):
        self.__cursor.close()
        self.__database.rollback() if any(errors) else self.__database.commit()
        self.close()

    def close(self):
        self.__database.close()
