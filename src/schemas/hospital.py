from marshmallow import fields

from . import BaseSchema

class HospitalSchema(BaseSchema):
    id = fields.Str()
    name = fields.Str()