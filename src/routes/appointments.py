from flask import Blueprint
from flask_restful import Api

from resources.appointment import ActiveAppointments, PastAppointments

APPOINTMENT_BLUEPRINT = Blueprint('appointment', __name__)

Api(APPOINTMENT_BLUEPRINT).add_resource(
    ActiveAppointments, '/appointments/active')

Api(APPOINTMENT_BLUEPRINT).add_resource(
    PastAppointments, '/appointments/past')
