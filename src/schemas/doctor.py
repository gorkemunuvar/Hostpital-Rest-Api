from marshmallow import Schema, fields


class DoctorSchema(Schema):
    id = fields.Str()
    name = fields.Str()
    surname = fields.Str()
    description = fields.Str()
    image_path = fields.Str()
    expertise = fields.Str()
    education = fields.Str()
    experience = fields.Str()
    achievements = fields.Str()
