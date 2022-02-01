from flask_restful import Resource

from services.patient import PatientService


class PatientTest(Resource):
    @classmethod
    def get(cls):
        try:
            is_patient_exist = PatientService.is_patient_exist()

            if not is_patient_exist:
                patient_id = PatientService.create_patient_id()
                PatientService.create_patient(str(patient_id))

                return {'message': 'Hasta Oluşturuldu.'}, 200
            else:
                return {'message': 'Hasta Zaten Kayıtlı.'}, 200
        except Exception as error:
            return {'message': f'Something went wrong. ({error})'.format(error=error)}, 500
