from flask import Blueprint
from flask_restful import Api

from resources.available_appointment_date import AvailableAppoinmentDate

AVAILABLE_APPOINTMENT_DATE_BLUEPRINT = Blueprint('available_appointment_date', __name__)

Api(AVAILABLE_APPOINTMENT_DATE_BLUEPRINT).add_resource(
    AvailableAppoinmentDate, '/available_appointment_dates')
