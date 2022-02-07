from flask_restful import Resource

from schemas.appointment import AppointmentSchema
from services.appointment import AppointmentService

appointments_schema = AppointmentSchema(many=True)


class ActiveAppointments(Resource):
    @classmethod
    def get(cls):
        try:
            appointments = AppointmentService.get_active_appointments()
            appointments_dict = appointments_schema.dump(appointments)
        except Exception as error:
            print(error)
            return {'message': f'Something went wrong. ({error})'.format(error=error)}

        return {'appointments': appointments_dict}, 200


class PastAppointments(Resource):
    @classmethod
    def get(cls):
        try:
            appointments = AppointmentService.get_past_appointments()
            appointments_dict = appointments_schema.dump(appointments)
        except Exception as error:
            print(error)
            return {'message': f'Something went wrong. ({error})'.format(error=error)}, 500

        return {'appointments': appointments_dict}, 200