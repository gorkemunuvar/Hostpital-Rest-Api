from flask import request
from flask_restful import Resource

from models.appointment import Appointment
from schemas.appointment import AppointmentSchema
from services.appointment import AppointmentService

appointment_schema = AppointmentSchema()
appointments_schema = AppointmentSchema(many=True)


class CreateAppointment(Resource):
    @classmethod
    def post(cls):
        try:
            appointment_dict = request.get_json()
            appointment = appointment_schema.load(appointment_dict)

            appointment_taken = AppointmentService.is_appointment_taken(
                appointment
            )

            if appointment_taken:
                return {'message': 'Appointment is already taken.'}, 409

            appointment_dict['id'] = AppointmentService.create_appointment_id()

            appointment = Appointment(**appointment_dict)

            AppointmentService.create_appointment(appointment)

            return {'message': 'Appointment created succesfully.'}, 201
        except Exception as error:
            print(error)
            return {'message': f'Something went wrong. ({error})'.format(error=error)}, 500


class ActiveAppointments(Resource):
    @classmethod
    def get(cls):
        try:
            appointments = AppointmentService.get_active_appointments()
            appointments_dict = appointments_schema.dump(appointments)

            return {'appointments': appointments_dict}, 200
        except Exception as error:
            print(error)
            return {'message': f'Something went wrong. ({error})'.format(error=error)}, 500


class PastAppointments(Resource):
    @classmethod
    def get(cls):
        try:
            appointments = AppointmentService.get_past_appointments()
            appointments_dict = appointments_schema.dump(appointments)

            return {'appointments': appointments_dict}, 200
        except Exception as error:
            print(error)
            return {'message': f'Something went wrong. ({error})'.format(error=error)}, 500
