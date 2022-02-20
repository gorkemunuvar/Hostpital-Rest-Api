from flask import Blueprint
from flask_restful import Api

from resources.available_hour import (AvailableHoursByDoctorId,
                                      AvailableHoursByProfession)

AVAILABLE_APPOINTMENT_TIME_BLUEPRINT = Blueprint(
    'available_time', __name__)

Api(AVAILABLE_APPOINTMENT_TIME_BLUEPRINT).add_resource(
    AvailableHoursByDoctorId, '/doctors/<string:id>/available_dates/<string:date>/available_times')


Api(AVAILABLE_APPOINTMENT_TIME_BLUEPRINT).add_resource(
    AvailableHoursByProfession, '/available_dates/<string:date>/available_times')
