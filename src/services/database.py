from __future__ import annotations
import cx_Oracle as oracle


class Connection(oracle.Connection):
    __connection = None

    @classmethod
    def create(cls) -> Connection:
        """Returns a singleton cx_Oracle.Connection object."""

        if not cls.__connection or not cls.__is_open():
            cls.__connection = oracle.connect(
                user="sys",
                password="123",
                dsn="localhost/orcl",
                mode=oracle.SYSDBA
            )

            print('INFO: CONNECTION CREATED AGAIN')

        return cls.__connection

    @staticmethod
    def execute(connection: Connection, query: str) -> oracle.Cursor:
        cursor = connection.cursor()

        return cursor.execute(query)

    @classmethod
    def __is_open(cls) -> bool:
        """Returns true if the connection object is alive."""

        try:
            return cls.__connection.ping() is None
        except:
            return False
