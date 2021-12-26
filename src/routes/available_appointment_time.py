from flask import Blueprint
from flask_restful import Api

from resources.available_appointment_time import AvailableAppoinmentTime

AVAILABLE_APPOINTMENT_TIME_BLUEPRINT = Blueprint(
    'available_appointment_time', __name__)

Api(AVAILABLE_APPOINTMENT_TIME_BLUEPRINT).add_resource(
    AvailableAppoinmentTime, '/doctors/<string:id>/available_dates/<string:date>/available_appointment_times')
