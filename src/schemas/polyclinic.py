import imp
from marshmallow import Schema, fields

from .doctor import DoctorSchema


class PolyclinicSchema(Schema):
    id = fields.Str()
    hospital_id = fields.Str()
    title = fields.Str()
    description = fields.Str()
    image_path = fields.Str()
    doctors = fields.List(fields.Nested(lambda: DoctorSchema()))
    # doctors = fields.List(fields.Pluck(DoctorSchema(many=True), "doctors"))
