from flask_restful import Resource

from services.available_appointment_date import AvailableAppoinmentDateService


class AvailableAppoinmentDate(Resource):
    @classmethod
    def get(cls, id: str):
        try:
            availableAppoinmentDates = AvailableAppoinmentDateService.get_avaiable_appoinment_dates_by_doctor_id(
                id)

            if availableAppoinmentDates:
                return {'available_appointment_dates': availableAppoinmentDates}, 200

            return {'message': 'Available appointments not found!'}, 404
        except Exception as error:
            print(error)
            return {'message': f'Something went wrong. ({error})'.format(error=error)}, 500
