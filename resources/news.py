from flask import request, abort
from flask_restful import Resource
from marshmallow import Schema, fields

from test_data.news import test_news_data


class NewsQuerySchema(Schema):
    page = fields.Str()
    per_page = fields.Str()


schema = NewsQuerySchema()


class News(Resource):
    @classmethod
    def get(self):
        # Defaults
        page = 1
        per_page = 5

        query_params = request.args
        errors = schema.validate(query_params)

        if errors:
            abort(400, str(errors))

        if query_params.__contains__('page'):
            page = int(query_params['page'])

        if query_params.__contains__('per_page'):
            per_page = int(query_params['per_page'])

        start = page * per_page - per_page
        end = page * per_page

        return {'news': test_news_data[start:end]}, 200
