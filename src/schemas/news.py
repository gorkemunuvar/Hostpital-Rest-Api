from marshmallow import fields

from . import BaseSchema


class NewsSchema(BaseSchema):
    title = fields.Str()
    description = fields.Str()
    date = fields.Str()
    image_path = fields.Str()
