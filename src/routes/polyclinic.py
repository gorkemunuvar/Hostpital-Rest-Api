from flask import Blueprint
from flask_restful import Api

from resources.polyclinic import Polyclinics, SearchPolyclinics

POLYCLINIC_BLUEPRINT = Blueprint('polyclinic', __name__)

Api(POLYCLINIC_BLUEPRINT).add_resource(
    Polyclinics, '/polyclinics')

Api(POLYCLINIC_BLUEPRINT).add_resource(
    SearchPolyclinics, '/polyclinics/search/<string:search_string>')
