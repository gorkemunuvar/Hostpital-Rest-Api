from flask_restful import Resource

from services.available_appointment_time import AvailableAppoinmentTimeService


class AvailableAppoinmentTime(Resource):
    @classmethod
    def get(cls, id: str, date: str):
        try:
            date = format_date_input(date)
            
            availableAppoinmentTimes = AvailableAppoinmentTimeService.get_avaiable_appoinment_times_by_doctor_id_and_date(
                id, date
                #'DR582', '2021.12.29'
            )

            if availableAppoinmentTimes:
                return {'available_appointment_times': availableAppoinmentTimes}, 200

            return {'message': 'Available times not found!'}, 404
        except Exception as error:
            print(error)
            return {'message': f'Something went wrong. ({error})'.format(error=error)}, 500


def format_date_input(date: str) -> str:
    """yyyy-mm-dd -> yyyy/mm/dd"""
    return date.replace('-', '/')
