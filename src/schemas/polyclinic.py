from marshmallow import fields

from . import BaseSchema
from .doctor import DoctorSchema


class PolyclinicSchema(BaseSchema):
    id = fields.Str()
    hospital_id = fields.Str()
    title = fields.Str()
    description = fields.Str()
    image_path = fields.Str()
    doctors = fields.List(fields.Nested(lambda: DoctorSchema()))