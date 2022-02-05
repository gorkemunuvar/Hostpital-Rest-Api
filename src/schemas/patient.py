from marshmallow import fields

from . import BaseSchema

class PatientSchema(BaseSchema):
    id = fields.Str()
    name = fields.Str()
    surname = fields.Str()
    father = fields.Str()
    birthday = fields.Str()
    phone_number = fields.Str()

