from flask import Blueprint
from flask_restful import Api

from resources.doctor import Doctors, DoctorById, DoctorsByProfessionId, SearchDoctor

DOCTOR_BLUEPRINT = Blueprint('doctor', __name__)

Api(DOCTOR_BLUEPRINT).add_resource(
    Doctors, '/doctors')
Api(DOCTOR_BLUEPRINT).add_resource(
    DoctorById, '/doctors/<string:id>')
Api(DOCTOR_BLUEPRINT).add_resource(
    SearchDoctor, '/doctors/search/<string:search_text>')
Api(DOCTOR_BLUEPRINT).add_resource(
    DoctorsByProfessionId, '/professions/<string:id>/doctors')
