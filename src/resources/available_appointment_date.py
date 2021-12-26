from flask_restful import Resource

from services.available_appointment_date import AvailableAppoinmentDateService


class AvailableAppoinmentDate(Resource):
    @classmethod
    def get(cls):
        availableAppoinmentDates = AvailableAppoinmentDateService.get_avaiable_appoinment_dates()

        return {'available_appointment_dates': availableAppoinmentDates}, 200
