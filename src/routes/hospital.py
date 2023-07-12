from flask import Blueprint
from flask_restful import Api

from resources.hostpital import Hospitals

HOSPITAL_BLUEPRINT = Blueprint('hospital', __name__)

Api(HOSPITAL_BLUEPRINT).add_resource(Hospitals, '/hospitals')
