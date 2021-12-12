from flask import Blueprint
from flask_restful import Api

from resources.expertise import ExperticesByPolyclinicId

EXPERTISE_BLUEPRINT = Blueprint('expertise', __name__)

Api(EXPERTISE_BLUEPRINT).add_resource(
    ExperticesByPolyclinicId, '/polyclinics/<string:id>/expertises')
