from flask import Blueprint
from flask_restful import Api

from resources.available_date import (AvailableAppointmentDatesByDoctorId,
                                                  AvailableAppointmentDatesByProfession)

AVAILABLE_APPOINTMENT_DATE_BLUEPRINT = Blueprint(
    'available_date', __name__)

Api(AVAILABLE_APPOINTMENT_DATE_BLUEPRINT).add_resource(
    AvailableAppointmentDatesByDoctorId, '/doctors/<string:id>/available-dates')

Api(AVAILABLE_APPOINTMENT_DATE_BLUEPRINT).add_resource(
    AvailableAppointmentDatesByProfession, '/professions/<string:profession_id>/available-dates')
