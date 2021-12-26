from flask_restful import Resource

from services.available_appointment_date import AvailableAppoinmentDateService


class AvailableAppoinmentDate(Resource):
    @classmethod
    def get(cls, id: str):
        availableAppoinmentDates = AvailableAppoinmentDateService.get_avaiable_appoinment_dates_by_doctor_id(
            id)

        if availableAppoinmentDates:
            return {'available_appointment_dates': availableAppoinmentDates}, 200

        return {'message': 'Available appointments not found!'}, 404
