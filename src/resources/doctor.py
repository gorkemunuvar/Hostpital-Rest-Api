from flask import request, abort
from flask_restful import Resource

from test_data.doctors import test_doctors_data
from services.doctor import DoctorService
from schemas.doctor import DoctorSchema
from schemas.pagination import PaginationSchema

pagination_schema = PaginationSchema()
doctor_schema = DoctorSchema()
doctors_schema = DoctorSchema(many=True)


class DoctorById(Resource):
    @classmethod
    def get(cls, id):
        if int(id) > len(test_doctors_data) or int(id) < 1:
            return {'message': 'The doctor not found.'}, 404

        doctor = DoctorService.get_doctor_by_id(id)
        doctor_dict = doctor_schema.dump(doctor)

        if doctor:
            return {'doctor': doctor_dict}, 200

        return {'message': 'Wrong input.'}, 404


class Doctors(Resource):
    @classmethod
    def get(cls):
        # Defaults
        page = 1
        per_page = 5

        query_params = request.args
        errors = pagination_schema.validate(query_params)

        if errors:
            abort(400, str(errors))

        if query_params.__contains__('page'):
            page = int(query_params['page'])

        if query_params.__contains__('per_page'):
            per_page = int(query_params['per_page'])

        doctors = DoctorService.get_doctors(page, per_page)
        doctors_dict = doctors_schema.dump(doctors)

        return {'doctors': doctors_dict}, 200


class SearchDoctor(Resource):
    @classmethod
    def get(cls, search_text):
        doctors = DoctorService.search_doctor(search_text)
        doctors_dict = doctors_schema.dump(doctors)

        return {'search_result': doctors_dict}, 200


class DoctorsByProfessionId(Resource):
    @classmethod
    def get(cls, id):
        doctors = DoctorService.get_doctors_by_profession_id(id)

        if doctors:
            doctors_dict = doctors_schema.dump(doctors)
            return {'doctors': doctors_dict}, 200

        return {'message': 'Doctors not found!'}, 404
