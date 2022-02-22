from flask import request
from flask_restful import Resource
from datetime import datetime

from models.appointment import Appointment
from core.utils.schemas.appointment import AppointmentSchema
from services.appointment import AppointmentService
from core.utils.string_handler import StringHandler

appointment_schema = AppointmentSchema()
appointments_schema = AppointmentSchema(many=True)


class CreateAppointment(Resource):
    @classmethod
    def post(cls):
        try:
            appointment_dict = request.get_json()
            formatted_date = StringHandler.format_date_input(
                appointment_dict['date']
            )

            appointment_dict['date'] = datetime.strptime(
                formatted_date, "%Y/%m/%d").strftime("%d-%m-%Y")

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
    def get(cls, patient_id: str):
        try:
            appointments = AppointmentService.get_active_appointments(
                patient_id)
            appointments_dict = appointments_schema.dump(appointments)

            return {'appointments': appointments_dict}, 200
        except Exception as error:
            print(error)
            return {'message': f'Something went wrong. ({error})'.format(error=error)}, 500


class PastAppointments(Resource):
    @classmethod
    def get(cls, patient_id: str):
        try:
            appointments = AppointmentService.get_past_appointments(patient_id)
            appointments_dict = appointments_schema.dump(appointments)

            return {'appointments': appointments_dict}, 200
        except Exception as error:
            print(error)
            return {'message': f'Something went wrong. ({error})'.format(error=error)}, 500


class CancelAppointment(Resource):
    @classmethod
    def put(cls, appointment_id):
        try:
            is_appointment_exist = AppointmentService.is_appointment_exist(
                appointment_id
            )

            if is_appointment_exist:
                AppointmentService.cancel_appointment(appointment_id)
                return {'message': 'Appointment deleted succesfully.'}, 200

            return {'message': 'Appointment not found.'}, 404

    
        except Exception as error:
            print(error)
            return {'message': f'Something went wrong. ({error})'.format(error=error)}, 500
