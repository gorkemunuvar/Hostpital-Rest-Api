from flask_restful import Resource

from services.patient import PatientService


class Patient(Resource):
    @classmethod
    def get(cls):
        try:
            patient = PatientService.get_patient()

            if patient:
                return {'message': 'Patient ID has been already created.',
                        'patient': {
                            'id':  patient.id
                        }}, 200
            else:
                patient_id = PatientService.create_patient_id()
                PatientService.create_patient(str(patient_id))

                return {'message': 'Patient ID created.',
                        'patient': {
                            'id': patient_id
                        }}, 201
        except Exception as error:
            return {'message': f'Something went wrong. ({error})'.format(error=error)}, 500
