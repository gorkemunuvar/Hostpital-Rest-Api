from marshmallow import fields

from . import BaseSchema

class DoctorSchema(BaseSchema):
    id = fields.Str()
    polyclinic_id = fields.Str()
    profession_id = fields.Str()
    name = fields.Str()
    surname = fields.Str()
    father = fields.Str()
    description = fields.Str()
    image_path = fields.Str()
    profession = fields.Str()
    education = fields.Str()
    experience = fields.Str()
    achievements = fields.Str()
