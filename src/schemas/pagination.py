from marshmallow import Schema, fields

class PaginationSchema(Schema):
    page = fields.Str()
    per_page = fields.Str()