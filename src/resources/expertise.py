from flask_restful import Resource

from schemas.expertise import ExpertiseSchema
from services.expertise import ExpertiseService

expertises_schmea = ExpertiseSchema(many=True)

class ExperticesByPolyclinicId(Resource):
    @classmethod
    def get(cls, id):
        expertises = ExpertiseService.get_expertises_by_polyclinic_id(id)

        if expertises:
            expertises_dict = expertises_schmea.dump(expertises)

            return {'expertises': expertises_dict}, 200

        return {'message': 'polyclinic_id not found'}, 404

