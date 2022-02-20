from flask_restful import Resource

from services.available_hour import AvailableAppoinmentTimeService


class AvailableAppoinmentTimeByDoctorId(Resource):
    @classmethod
    def get(cls, date: str, id: str = None):
        try:
            date = format_date_input(date)

            availableAppoinmentTimes = AvailableAppoinmentTimeService.get_avaiable_appoinment_times(
                date, id
            )

            if availableAppoinmentTimes:
                return {'available_times': availableAppoinmentTimes}, 200

            return {'message': 'Available times not found!'}, 404
        except Exception as error:
            print(error)
            return {'message': f'Something went wrong. ({error})'.format(error=error)}, 500


class AvailableAppoinmentTimeByProfession(Resource):
    @classmethod
    def get(cls, date: str):
        try:
            date = format_date_input(date)

            availableTimes = AvailableAppoinmentTimeService.get_avaiable_appoinment_times(
                date)

            if availableTimes:
                return {'available_times': availableTimes}, 200

            return {'message': 'Available times not found!'}, 404
        except Exception as error:
            print(error)
            return {'message': f'Something went wrong. ({error})'.format(error=error)}, 500


def format_date_input(date: str) -> str:
    """yyyy-mm-dd -> yyyy/mm/dd"""
    return date.replace('-', '/')
