from flask import request, abort
from flask_restful import Resource
from marshmallow import Schema, fields

class CampaignsQuerySchema(Schema):
    page = fields.Str()
    per_page = fields.Str()

schema = CampaignsQuerySchema()


class Campaigns(Resource):
    @classmethod
    def get(self):
        errors = schema.validate(request.args)
        
        if errors:
            abort(400, str(errors))

        return {'campaigns': request.args}