from flask import request, abort
from flask_restful import Resource
from marshmallow import Schema, fields

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

        return {'todo_id': request.args}