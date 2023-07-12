from flask import Blueprint
from flask_restful import Api

from resources.doctor import (AllDoctors, DoctorById, DoctorsByPolyclinicId,
                              DoctorsByProfessionId, SearchDoctor)

DOCTOR_BLUEPRINT = Blueprint('doctor', __name__)

Api(DOCTOR_BLUEPRINT).add_resource(
    AllDoctors, '/doctors/<int:page>')

Api(DOCTOR_BLUEPRINT).add_resource(
    DoctorById, '/doctors/<string:id>')

Api(DOCTOR_BLUEPRINT).add_resource(
    SearchDoctor, '/doctors/search/<string:search_string>')

Api(DOCTOR_BLUEPRINT).add_resource(
    DoctorsByPolyclinicId, '/polyclinics/<string:id>/doctors')

Api(DOCTOR_BLUEPRINT).add_resource(
    DoctorsByProfessionId, '/professions/<string:id>/doctors')
