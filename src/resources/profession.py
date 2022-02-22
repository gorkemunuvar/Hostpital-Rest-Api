from flask_restful import Resource

from core.utils.schemas.profession import ProfessionSchema
from services.profession import ProfessionService

professions_schmea = ProfessionSchema(many=True)

class ProfessionsByPolyclinicId(Resource):
    @classmethod
    def get(cls, id):
        try:
            professions = ProfessionService.get_professions_by_polyclinic_id(id)

            if professions:
                professions_dict = professions_schmea.dump(professions)

                return {'professions': professions_dict}, 200

            return {'message': 'polyclinic_id not found'}, 404
        except Exception as error:
            print(error)
            return {'message': f'Something went wrong. ({error})'.format(error=error)}, 500

