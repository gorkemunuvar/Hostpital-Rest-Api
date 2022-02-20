from marshmallow import fields

from . import BaseSchema

class PaginationSchema(BaseSchema):
    page = fields.Str()
    per_page = fields.Str()