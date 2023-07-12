from flask import Blueprint
from flask_restful import Api

from resources.appointment import (ActiveAppointments, PastAppointments,
                                   CreateAppointment, CancelAppointment)

APPOINTMENT_BLUEPRINT = Blueprint('appointment', __name__)


Api(APPOINTMENT_BLUEPRINT).add_resource(
    CreateAppointment, '/appointments')

Api(APPOINTMENT_BLUEPRINT).add_resource(
    ActiveAppointments, '/patients/<string:patient_id>/appointments/active')

Api(APPOINTMENT_BLUEPRINT).add_resource(
    PastAppointments, '/patients/<string:patient_id>/appointments/past')


Api(APPOINTMENT_BLUEPRINT).add_resource(
    CancelAppointment, '/appointments/<string:appointment_id>')
