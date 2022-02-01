from flask import Blueprint
from flask_restful import Api

from resources.patient_test import PatientTest

PATIENT_TEST_BLUEPRINT = Blueprint('patient', __name__)

Api(PATIENT_TEST_BLUEPRINT).add_resource(PatientTest, '/patient')
