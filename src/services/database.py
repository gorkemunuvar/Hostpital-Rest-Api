import cx_Oracle as oracle


class Database:
    __connection = None

    @classmethod
    def connect(cls):
        """Returns a singleton Connection object."""

        if not cls.__connection:
            cls.__connection = oracle.connect(
                user="sys",
                password="123",
                dsn="localhost/orcl",
                mode=oracle.SYSDBA
            )

        return cls.__connection
