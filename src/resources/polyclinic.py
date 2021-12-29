from flask_restful import Resource

from schemas.polyclinic import PolyclinicSchema
from services.polyclinic import PolyclinicService

polyclinic_schmea = PolyclinicSchema()
polyclinics_schmea = PolyclinicSchema(many=True)


class Polyclinics(Resource):
    @classmethod
    def get(cls):
        polyclinics = PolyclinicService.get_polyclinics()
        polyclinics_dict = polyclinics_schmea.dump(polyclinics)

        return {'polyclinics': polyclinics_dict}, 200


class SearchPolyclinics(Resource):
    @classmethod
    def get(cls, search_text):
        polyclinics = PolyclinicService.search_polyclinics(search_text)
        polyclinics_dict = polyclinics_schmea.dump(polyclinics)

        return {'search_result': polyclinics_dict}, 200
