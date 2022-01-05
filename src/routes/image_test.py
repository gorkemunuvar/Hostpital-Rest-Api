from flask import Blueprint
from flask_restful import Api

from resources.image_test import ImageTest

IMAGE_TEST_BLUEPRINT = Blueprint('image', __name__)

Api(IMAGE_TEST_BLUEPRINT).add_resource(ImageTest, '/image')
