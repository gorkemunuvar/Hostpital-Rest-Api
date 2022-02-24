from flask import Blueprint
from flask_restful import Api

from resources.news import News

NEWS_BLUEPRINT = Blueprint('news', __name__)

Api(NEWS_BLUEPRINT).add_resource(News, '/news/<int:page>')
