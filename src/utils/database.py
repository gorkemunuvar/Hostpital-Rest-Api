from __future__ import annotations
from typing import Union

import cx_Oracle as oracle

from utils.config import DevelopmentConfig

configs = DevelopmentConfig()


class Connection(oracle.Connection):
    __connection = None

    @classmethod
    def create(cls) -> Connection:
        """Returns a singleton cx_Oracle.Connection object."""

        if not cls.__connection or not cls.__is_open():
            dsn = oracle.makedsn(
                configs.DB_URL, configs.DB_PORT, service_name=configs.DB_SERVICE_NAME,
            )

            cls.__connection = oracle.connect(
                user=configs.DB_USERNAME, password=configs.DB_PASSWORD, dsn=dsn, encoding='UTF-8'
            )

            print('INFO: CONNECTION CREATED')

        return cls.__connection

    @staticmethod
    def execute(connection: Connection, query: str) -> Union[oracle.Cursor, None]:
        cursor = connection.cursor()

        return cursor.execute(query)

    @classmethod
    def __is_open(cls) -> bool:
        """Returns true if the connection object is alive."""

        try:
            return cls.__connection.ping() is None
        except:
            return False
