from flask import request
from flask_restful import Resource

from schemas.appointment import AppointmentSchema
from services.appointment import AppointmentService

appointments_schema = AppointmentSchema(many=True)


class CreateAppointment(Resource):
    @classmethod
    def post(cls):
        try:
            appointment_dict = request.get_json()

            appointment_taken = AppointmentService.is_appointment_taken()
            if appointment_taken:
                return {'message': 'Appointment is already taken.'}, 200

            appointment_id = AppointmentService.create_appointment_id()
            AppointmentService.create_appointment()

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
