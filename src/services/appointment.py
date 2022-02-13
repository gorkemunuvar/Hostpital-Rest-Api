from typing import Union
from .database import Connection
from models.appointment import Appointment
from utils.string_handler import StringHandler
from utils.queries import (ACTIVE_APPOINTMENTS, PAST_APPOINTMENTS,
                           IS_APPOINTMENT_TAKEN, CREATE_APPOINTMENT_ID,
                           CREATE_APPOINTMENT)


class AppointmentService():
    @classmethod
    def create_appointment(cls) -> None:
        connection = Connection.create()
        cursor = Connection.execute(connection, CREATE_APPOINTMENT)
        connection.commit()

        if cursor:
            cursor.close()

    @classmethod
    def is_appointment_taken(cls) -> bool:
        connection = Connection.create()
        cursor = Connection.execute(connection, IS_APPOINTMENT_TAKEN)

        row = cursor.fetchone()

        if row:
            return True
        return False

    @classmethod
    def create_appointment_id(cls) -> Union[str, None]:
        connection = Connection.create()
        cursor = Connection.execute(connection, CREATE_APPOINTMENT_ID)

        row = cursor.fetchone()

        if row:
            return str(row[0])
        return None

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
