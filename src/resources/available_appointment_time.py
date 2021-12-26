from flask_restful import Resource

from services.available_appointment_time import AvailableAppoinmentTimeService


class AvailableAppoinmentTime(Resource):
    @classmethod
    def get(cls):
        availableAppoinmentTimes = AvailableAppoinmentTimeService.get_avaiable_appoinment_times()

        return {'available_appointment_times': availableAppoinmentTimes}, 200
