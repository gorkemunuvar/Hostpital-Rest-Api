from __future__ import annotations
import cx_Oracle as oracle


class Connection(oracle.Connection):
    __connection = None

    @classmethod
    def create(cls) -> Connection:
        """Returns a singleton cx_Oracle.Connection object."""

        if not cls.__connection:
            cls.__connection = oracle.connect(
                user="sys",
                password="123",
                dsn="localhost/orcl",
                mode=oracle.SYSDBA
            )

        return cls.__connection

    @staticmethod
    def execute(connection: Connection, query: str) -> oracle.Cursor:
        cursor = connection.cursor()

        return cursor.execute(query)
