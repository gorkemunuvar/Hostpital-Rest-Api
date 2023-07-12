from marshmallow import fields

from . import BaseSchema


class PolyclinicSchema(BaseSchema):
    id = fields.Str()
    title = fields.Str()
    description = fields.Str()
    image_base64 = fields.Str()
