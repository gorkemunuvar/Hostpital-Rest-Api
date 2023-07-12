from marshmallow import fields

from . import BaseSchema

class PatientSchema(BaseSchema):
    id = fields.Str(dump_only=True)
    name = fields.Str()
    surname = fields.Str()
    birthday = fields.Str()
    phone_number = fields.Str()

