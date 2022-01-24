from marshmallow import fields

from . import BaseSchema


class NewsSchema(BaseSchema):
    id = fields.Str()
    title = fields.Str()
    description = fields.Str()
    date = fields.Str()
    image_base64 = fields.Str()
