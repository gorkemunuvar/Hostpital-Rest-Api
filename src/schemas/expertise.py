from marshmallow import fields

from . import BaseSchema


class ExpertiseSchema(BaseSchema):
    id = fields.Str()
    polyclinic_id = fields.Str()
    name = fields.Str()
    