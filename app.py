import cx_Oracle
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey321'


def connect_db() -> None:
    connection = cx_Oracle.connect(
        user="sys",
        password="123",
        dsn="localhost/orcl",
        mode=cx_Oracle.SYSDBA
    )

    cursor = connection.cursor()
    cursor.execute(
        """ SELECT profs, isim 
            FROM ng_his_kabuzman
            WHERE kiosk='X'order by isim"""
    )

    for profs, name in cursor:
        print("Values:", profs, name)


if __name__ == '__main__':
    connect_db()
    app.run()