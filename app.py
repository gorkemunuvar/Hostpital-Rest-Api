import cx_Oracle
from flask import Flask
from flask_restful import Api

from resources.news import News
from resources.campaigns import Campaigns

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey321'

api = Api(app)

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


def set_api():
    api.add_resource(News, '/api/news/')
    api.add_resource(Campaigns, '/api/campaigns/')

if __name__ == '__main__':
    connect_db()
    set_api()

    app.run(debug=True)