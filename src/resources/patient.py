from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from services.patient import PatientService

class Patient(Resource):
    @classmethod
    def post(cls):
        try:
            patient_dict = request.get_json()

            patient_id = PatientService.search_patient_id(
                name=patient_dict['name'],
                surname=patient_dict['surname'],
                birthday=patient_dict['birthday']
            )

            if patient_id:

                return {'message': 'Patient ID has been already created.',
                        'patient': {
                            'id':  patient_id
                        }}, 200
            else:
                new_patient_id = PatientService.create_patient_id()

                PatientService.create_patient(
                    patient_id=new_patient_id, **patient_dict
                )

                return {'message': 'Patient ID created.',
                        'patient': {
                            'id': new_patient_id
                        }}, 201
        except Exception as error:
            print(error)
            return {'message': f'Something went wrong. ({error})'.format(error=error)}, 500
