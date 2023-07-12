from flask import Blueprint
from flask_restful import Api

from resources.profession import ProfessionsByPolyclinicId

PROFESSION_BLUEPRINT = Blueprint('profession', __name__)

Api(PROFESSION_BLUEPRINT).add_resource(
    ProfessionsByPolyclinicId, '/polyclinics/<string:id>/professions')
