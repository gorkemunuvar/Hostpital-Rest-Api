import json
import cx_Oracle
from flask import Flask
from flask_restful import Api

from resources.news import News
from resources.campaigns import Campaigns
from resources.hostpitals import Hospitals
from resources.doctors import Doctors, DoctorById, SearchDoctor
from resources.polyclinics import Polyclinics, PolyclinicById, SearchPolyclinic, PolyclinicsByHospitalId

from models.hospital import Hospital

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey321'

api = Api(app)


def init_db() -> None:
    connection = cx_Oracle.connect(
        user="sys",
        password="123",
        dsn="localhost/orcl",
        mode=cx_Oracle.SYSDBA
    )

    cursor = connection.cursor()
    cursor.execute("""select DBKOD,DBAD from NG_HIS_LNKDBS t""")

    print('----------------------------------')

    r = [dict((cursor.description[i][0], value) \
                for i, value in enumerate(row)) for row in cursor.fetchall()]
    print(json.dumps(r, indent=2))  #How to return name of table as well?



    # for profs, name in cursor:
    #     print("Values:", profs, name)

    print(dict(cursor))

    print(type(cursor))


def init_api():
    # News Endpoints
    api.add_resource(News, '/news')
    api.add_resource(Campaigns, '/campaigns')

    # Hospital Endpoints
    api.add_resource(Hospitals, '/hospitals')

    # Polyclinic Endpoints
    api.add_resource(Polyclinics, '/polyclinics')
    api.add_resource(PolyclinicById, '/polyclinics/<string:id>')
    api.add_resource(SearchPolyclinic,
                     '/polyclinics/search/<string:search_text>')
    api.add_resource(PolyclinicsByHospitalId,
                     '/hospitals/<string:hospital_id>/polyclinics')

    # Doctor Endpoints
    api.add_resource(Doctors, '/doctors')
    api.add_resource(DoctorById, '/doctors/<string:id>')
    api.add_resource(SearchDoctor, '/doctors/search/<string:search_text>')


if __name__ == '__main__':
    #init_db()
    hospital = Hospital()
    hospitals = hospital.fetch_hospitals()

    init_api()

    app.run(debug=True)
