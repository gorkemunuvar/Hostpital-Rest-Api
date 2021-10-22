from flask import request, abort
from flask_restful import Resource

from test_data.doctors import test_doctors_data
from schemas.pagination import PaginationSchema

schema = PaginationSchema()


class DoctorById(Resource):
    @classmethod
    def get(cls, id):
        if int(id) > len(test_doctors_data) or int(id) < 1:
            return {'message': 'The doctor not found.'}, 404

        for doctor in test_doctors_data:
            if doctor['id'] == id:
                return {'doctor': doctor}, 200

        return {'message': 'Wrong input.'}, 404


class Doctors(Resource):
    @classmethod
    def get(cls):
        # Defaults
        page = 1
        per_page = 5

        query_params = request.args
        errors = schema.validate(query_params)

        if errors:
            abort(400, str(errors))

        if query_params.__contains__('page'):
            page = int(query_params['page'])

        if query_params.__contains__('per_page'):
            per_page = int(query_params['per_page'])

        start = page * per_page - per_page
        end = page * per_page

        return {'doctors': test_doctors_data[start:end]}, 200
