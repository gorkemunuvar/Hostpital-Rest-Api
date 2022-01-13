import json
from flask import request, abort, send_file, make_response, jsonify
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

        try:
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
        except Exception as error:
            return {'message': f'Something went wrong. ({error})'.format(error=error)}

        return {'doctors': doctors_dict}, 200


class DoctorById(Resource):
    @classmethod
    def get(cls, id):
        from services.database import Connection
        from utils.queries import DOCTOR_BY_ID

        connection = Connection.create()
        cursor = connection.cursor()

        cursor = cursor.execute(DOCTOR_BY_ID)
        row = cursor.fetchone()

        for row in cursor:
            print(row[0])
            print(row[1])
            print(row[2])
            print(row[3])
            print(row[4])
            print(row[5])
            print(row[6])
            print(row[7])
            print(row[8])

        print('types of columns')

        # for column in row:
        #     print(type(column))

        # for row in cursor:
        #     image = row[5]

        #     print('type')
        #     print(type(image))

        #     dumped_image = json.dumps(str(image))

        # return send_file(dumped_image, mimetype='image/png'), 200

        # doctor = DoctorService.get_doctor_by_id(id)
        # doctor_dict = doctor_schema.dump(doctor)

        # if doctor:
        #     return {'doctor': doctor_dict}, 200

        # return {'message': 'Doctor not found..'}, 404


class DoctorsByPolyclinicId(Resource):
    @classmethod
    def get(cls, id):
        doctors_dict = {}

        try:
            doctors = DoctorService.get_doctors_by_polyclinic_id(id)

            if doctors:
                doctors_dict = doctors_schema.dump(doctors)
        except Exception as error:
            return {'message': f'Something went wrong. ({error})'.format(error=error)}

        return {'doctors': doctors_dict}, 200


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
    def get(cls, search_string):
        doctors_dict = {}

        try:
            doctors = DoctorService.search_doctors(search_string)
            doctors_dict = doctors_schema.dump(doctors)
        except Exception as error:
            return {'message': f'Something went wrong. ({error})'.format(error=error)}

        return {'search_result': doctors_dict}, 200
