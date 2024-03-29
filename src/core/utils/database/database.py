from __future__ import annotations
from typing import Union

import cx_Oracle as oracle

from core.utils.config import DevelopmentConfig

configs = DevelopmentConfig()


class Connection(oracle.Connection):
    __connection = None

    @classmethod
    def create(cls) -> Connection:
        """Returns a singleton cx_Oracle.Connection object."""

        if not cls.__connection or not cls.__is_open():
            cls.__create_real_test_db_connection()
            #cls.__create_local_db_connection()

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

    @classmethod
    def __create_real_test_db_connection(cls):
        dsn = oracle.makedsn(
            configs.DB_URL, configs.DB_PORT, service_name=configs.DB_SERVICE_NAME,
        )

        cls.__connection = oracle.connect(
            user=configs.DB_USERNAME, password=configs.DB_PASSWORD, dsn=dsn, encoding='UTF-8'
        )

    @classmethod
    def __create_local_db_connection(cls):
        cls.__connection = oracle.connect(
            user=configs.local_db.DB_USERNAME,
            password=configs.local_db.DB_PASSWORD,
            dsn=configs.local_db.DB_URL,
            mode=configs.local_db.DB_MODE
        )
