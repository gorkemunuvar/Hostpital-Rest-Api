import datetime
from marshmallow import Schema, fields


class NewsSchema(Schema):
    title = fields.Str()
    description = fields.Str()
    date = fields.Str()
    image_path = fields.Str()
