from marshmallow import fields

from . import BaseSchema


class ProfessionSchema(BaseSchema):
    id = fields.Str()
    polyclinic_id = fields.Str()
    name = fields.Str()
    type = fields.Str()    