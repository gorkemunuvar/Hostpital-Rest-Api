from flask import Blueprint
from flask_restful import Api

from resources.patient import Patient

PATIENT_BLUEPRINT = Blueprint('patient', __name__)

Api(PATIENT_BLUEPRINT).add_resource(Patient, '/create_patient')
