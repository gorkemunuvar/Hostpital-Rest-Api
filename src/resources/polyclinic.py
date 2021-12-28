from flask_restful import Resource

from test_data.polyclinics import test_polyclinics_data
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


class PolyclinicById(Resource):
    @classmethod
    def get(cls):
    #def get(cls, id):
        # if int(id) > len(test_polyclinics_data) or int(id) < 1:
        #     return {'message': 'The given id not found.'}, 404

        polyclinic_doctors = PolyclinicService.get_polyclinic_by_id()
        #polyclinic_doctors = PolyclinicService.get_polyclinic_by_id(id)
        return {'polyclinic_doctors': polyclinic_doctors}, 200

        
        #polyclinic_dict = polyclinic_schmea.dump(polyclinic)
        #return {'polyclinic_details': test_polyclinics_data[int(id) - 1]}, 200


class PolyclinicsByHospitalId(Resource):
    @classmethod
    def get(cls, id):
        polyclinics = PolyclinicService.get_polyclinics_by_hospital_id(id)

        if polyclinics:
            polyclinics_dict = polyclinics_schmea.dump(polyclinics)

            return {'polyclinics': polyclinics_dict}, 200

        return {'message': 'hospital_id not found'}, 404


class SearchPolyclinics(Resource):
    @classmethod
    def get(cls, search_text):
        polyclinics = PolyclinicService.search_polyclinics(search_text)
        polyclinics_dict = polyclinics_schmea.dump(polyclinics)

        return {'search_result': polyclinics_dict}, 200
