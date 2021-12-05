from marshmallow import Schema, fields

class HospitalSchema(Schema):
    id = fields.Str()
    name = fields.Str()