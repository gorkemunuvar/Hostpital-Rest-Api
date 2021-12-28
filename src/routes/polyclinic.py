from flask import Blueprint
from flask_restful import Api

from resources.polyclinic import Polyclinics, PolyclinicById, PolyclinicsByHospitalId, SearchPolyclinics

POLYCLINIC_BLUEPRINT = Blueprint('polyclinic', __name__)

Api(POLYCLINIC_BLUEPRINT).add_resource(
    Polyclinics, '/polyclinics')
Api(POLYCLINIC_BLUEPRINT).add_resource(
     PolyclinicById, '/polyclinic_doctors')
# Api(POLYCLINIC_BLUEPRINT).add_resource(
#     PolyclinicById, '/polyclinics/<string:id>')
Api(POLYCLINIC_BLUEPRINT).add_resource(
    SearchPolyclinics, '/polyclinics/search/<string:search_text>')
Api(POLYCLINIC_BLUEPRINT).add_resource(
    PolyclinicsByHospitalId, '/hospitals/<string:id>/polyclinics')
