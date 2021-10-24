from flask_restful import Resource

from test_data.polyclinics import test_polyclinics_data


class Polyclinics(Resource):
    @classmethod
    def get(cls):
        result = []
        for polyclinic in test_polyclinics_data:
            obj = {
                'id': polyclinic['id'],
                'title': polyclinic['title'],
                'description': polyclinic['description'],
                'image_path': polyclinic['image_path']

            }
            result.append(obj)

        return {'polyclinics': result}, 200


class PolyclinicById(Resource):
    @classmethod
    def get(cls, id):
        if int(id) > len(test_polyclinics_data) or int(id) < 1:
            return {'message': 'The given id not found.'}, 404

        return {'polyclinic_details': test_polyclinics_data[int(id) - 1]}, 200


class SearchPolyclinic(Resource):
    @classmethod
    def get(cls, search_text):
        result = []
        for polyclinic in test_polyclinics_data:
            if search_text.lower() in polyclinic['title'].lower():
                result.append(polyclinic)

        return {'search_result': result}, 200
