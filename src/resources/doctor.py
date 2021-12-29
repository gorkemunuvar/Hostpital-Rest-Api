from flask import request, abort
from flask_restful import Resource

from services.doctor import DoctorService
from schemas.doctor import DoctorSchema
from schemas.pagination import PaginationSchema

pagination_schema = PaginationSchema()
doctor_schema = DoctorSchema()
doctors_schema = DoctorSchema(many=True)


class AllDoctors(Resource):
    @classmethod
    def get(cls):
        page = 1
        per_page = 10

        query_params = request.args
        errors = pagination_schema.validate(query_params)

        if errors:
            abort(400, str(errors))

        if query_params.__contains__('page'):
            page = int(query_params['page'])

        if query_params.__contains__('per_page'):
            per_page = int(query_params['per_page'])

        doctors = DoctorService.get_all_doctors(page, per_page)
        doctors_dict = doctors_schema.dump(doctors)

        return {'doctors': doctors_dict}, 200


class DoctorById(Resource):
    @classmethod
    def get(cls, id):
        doctor = DoctorService.get_doctor_by_id(id)
        doctor_dict = doctor_schema.dump(doctor)

        if doctor:
            return {'doctor': doctor_dict}, 200

        return {'message': 'Doctor not found..'}, 404


class DoctorsByPolyclinicId(Resource):
    @classmethod
    def get(cls, id):
        doctors = DoctorService.get_doctors_by_polyclinic_id(id)

        if doctors:
            doctors_dict = doctors_schema.dump(doctors)
            return {'doctors': doctors_dict}, 200

        return {'message': 'Doctors not found!'}, 404


class DoctorsByProfessionId(Resource):
    @classmethod
    def get(cls, id):
        doctors = DoctorService.get_doctors_by_profession_id(id)

        if doctors:
            doctors_dict = doctors_schema.dump(doctors)
            return {'doctors': doctors_dict}, 200

        return {'message': 'Doctors not found!'}, 404


class SearchDoctor(Resource):
    @classmethod
    def get(cls, search_text):
        doctors = DoctorService.search_doctor(search_text)
        doctors_dict = doctors_schema.dump(doctors)

        return {'search_result': doctors_dict}, 200
