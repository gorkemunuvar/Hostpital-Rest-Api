from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from services.patient import PatientService
from schemas.patient import PatientSchema

class Patient(Resource):
    @classmethod
    def post(cls):
        try:
            patient_dict = request.get_json()
            patient = PatientService.get_patient(**patient_dict)

            if patient:
                return {'message': 'Patient ID has been already created.',
                        'patient': {
                            'id':  patient.id
                        }}, 200
            else:
                patient_id = PatientService.create_patient_id()
                PatientService.create_patient(patient_id=patient_id,
                                              **patient_dict)

                return {'message': 'Patient ID created.',
                        'patient': {
                            'id': patient_id
                        }}, 201
        except Exception as error:
            print(error)
            return {'message': f'Something went wrong. ({error})'.format(error=error)}, 500
