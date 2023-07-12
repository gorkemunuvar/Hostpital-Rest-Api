from marshmallow import fields

from . import BaseSchema

class AppointmentSchema(BaseSchema):
    id = fields.Str()
    date = fields.Str()
    time = fields.Str()
    profession_id = fields.Str()
    profession_name = fields.Str()
    doctor_id = fields.Str()
    doctor_name = fields.Str()
    doctor_surname = fields.Str()
    patient_id = fields.Str()
    patient_name = fields.Str()
    patient_surname = fields.Str()
    patient_father = fields.Str()
    patient_birthday = fields.Str()
    note = fields.Str()