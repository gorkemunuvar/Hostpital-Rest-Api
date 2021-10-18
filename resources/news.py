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
        errors = schema.validate(request.args)

        if errors:
            abort(400, str(errors))

        return {'news': test_news_data}, 200
