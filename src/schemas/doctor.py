from marshmallow import fields

from . import BaseSchema

class DoctorSchema(BaseSchema):
    id = fields.Str()
    name = fields.Str()
    surname = fields.Str()
    description = fields.Str()
    image_path = fields.Str()
    expertise = fields.Str()
    education = fields.Str()
    experience = fields.Str()
    achievements = fields.Str()
