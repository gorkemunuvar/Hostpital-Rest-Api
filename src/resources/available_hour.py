from flask_restful import Resource

from services.available_hour import AvailableHourService
from utils.string_handler import StringHandler


class AvailableHoursByDoctorId(Resource):
    @classmethod
    def get(cls, date: str, id: str = None):
        try:
            date = StringHandler.format_date_input(date)
            available_hours = AvailableHourService.get_avaiable_hours(date, id)
            
            if available_hours:
                return {'available_times': available_hours}, 200

            return {'message': 'Available times not found!'}, 404
        except Exception as error:
            print(error)
            return {'message': f'Something went wrong. ({error})'.format(error=error)}, 500


class AvailableHoursByProfession(Resource):
    @classmethod
    def get(cls, date: str):
        try:
            date = StringHandler.format_date_input(date)
            available_hours = AvailableHourService.get_avaiable_hours(date)
            
            if available_hours:
                return {'available_times': available_hours}, 200

            return {'message': 'Available times not found!'}, 404
        except Exception as error:
            print(error)
            return {'message': f'Something went wrong. ({error})'.format(error=error)}, 500

