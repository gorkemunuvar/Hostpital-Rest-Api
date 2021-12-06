from os import name
from flask_restful import Resource

from models.hospital import Hospital
from schemas.hospital import HospitalSchema
from services.hospital import HospitalService

hospitals_schema = HospitalSchema(many=True)


class Hospitals(Resource):
    @classmethod
    def get(self):
        hospitals = HospitalService.get_hospitals()
        hospitals_dict = hospitals_schema.dump(hospitals)

        return {'hospitals': hospitals_dict}, 200
