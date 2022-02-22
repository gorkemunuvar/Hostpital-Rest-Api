from flask_restful import Resource

from core.utils.schemas.polyclinic import PolyclinicSchema
from services.polyclinic import PolyclinicService

polyclinic_schmea = PolyclinicSchema()
polyclinics_schmea = PolyclinicSchema(many=True)


class Polyclinics(Resource):
    @classmethod
    def get(cls):
        try:
            polyclinics = PolyclinicService.get_polyclinics()
            polyclinics_dict = polyclinics_schmea.dump(polyclinics)
    
            return {'polyclinics': polyclinics_dict}, 200
        except Exception as error:
            print(error)
            return {'message': f'Something went wrong. ({error})'.format(error=error)}, 500



class SearchPolyclinics(Resource):
    @classmethod
    def get(cls, search_string):
        try:
            polyclinics = PolyclinicService.search_polyclinics(search_string)
            polyclinics_dict = polyclinics_schmea.dump(polyclinics)
    
            return {'search_result': polyclinics_dict}, 200
        except Exception as error:
            print(error)
            return {'message': f'Something went wrong. ({error})'.format(error=error)}, 500
        
