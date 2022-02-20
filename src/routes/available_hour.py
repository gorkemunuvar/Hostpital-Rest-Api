from flask import Blueprint
from flask_restful import Api

from resources.available_hour import (AvailableAppoinmentTimeByDoctorId,
                                                  AvailableAppoinmentTimeByProfession)

AVAILABLE_APPOINTMENT_TIME_BLUEPRINT = Blueprint(
    'available_time', __name__)

Api(AVAILABLE_APPOINTMENT_TIME_BLUEPRINT).add_resource(
    AvailableAppoinmentTimeByDoctorId, '/doctors/<string:id>/available_dates/<string:date>/available_times')


Api(AVAILABLE_APPOINTMENT_TIME_BLUEPRINT).add_resource(
    AvailableAppoinmentTimeByProfession, '/available_dates/<string:date>/available_times')
