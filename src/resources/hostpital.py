from os import name
from flask_restful import Resource

from models.hospital import Hospital
from schemas.hospital import HospitalSchema
from test_data.hospitals import test_hospitals_data

hospitals_schema = HospitalSchema(many=True)


class Hospitals(Resource):
    @classmethod
    def get(self):
        hospitals = []
        for item in test_hospitals_data:
            hospital = Hospital(id=item['id'], name=item['name'])
            hospitals.append(hospital)

        hospitals_dict = hospitals_schema.dump(hospitals)

        return {'hospitals': hospitals_dict}, 200
