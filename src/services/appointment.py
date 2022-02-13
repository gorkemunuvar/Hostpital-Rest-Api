from .database import Connection
from models.appointment import Appointment
from utils.queries import ACTIVE_APPOINTMENTS, PAST_APPOINTMENTS, CREATE_APPOINTMENT
from utils.string_handler import StringHandler


class AppointmentService():
    @classmethod
    def create_appointment(cls) -> None:
        connection = Connection.create()
        cursor = Connection.execute(connection, CREATE_APPOINTMENT)
        connection.commit()
        
        if cursor:
            cursor.close()

    @classmethod
    def get_active_appointments(cls) -> list[Appointment]:
        return cls.__get_appointments(ACTIVE_APPOINTMENTS)

    @classmethod
    def get_past_appointments(cls) -> list[Appointment]:
        return cls.__get_appointments(PAST_APPOINTMENTS)

    @classmethod
    def __get_appointments(cls, query: str) -> list[Appointment]:
        connection = Connection.create()
        cursor = Connection.execute(connection, query)

        appointments = []
        if cursor:
            for row in cursor:
                formatted_date = StringHandler.select_first_element_of(
                    str(row[0]))

                appointment = Appointment(date=formatted_date, time=row[1],
                                          profession_id=row[2], profession_name=row[3],
                                          doctor_id=row[4], doctor_name=row[5],
                                          doctor_surname=row[6], patient_name=row[7],
                                          patient_surname=row[8], patient_father=row[9],
                                          patient_birthday=row[10])
                appointments.append(appointment)

            cursor.close()

        return appointments
