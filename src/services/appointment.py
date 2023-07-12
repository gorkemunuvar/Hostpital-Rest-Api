from sqlite3 import connect
from typing import Union

from core.utils.database.database import Connection
from core.utils.schemas.appointment import AppointmentSchema
from models.appointment import Appointment

from core.utils.string_handler import StringHandler
from core.utils.database.queries.ru.appointment import (ACTIVE_APPOINTMENTS, PAST_APPOINTMENTS,
                                                        IS_APPOINTMENT_TAKEN, CREATE_APPOINTMENT_ID,
                                                        CREATE_APPOINTMENT, CANCEL_APPOINTMENT,
                                                        IS_APPOINTMENT_EXIST)

appointment_schema = AppointmentSchema()


class AppointmentService():
    @classmethod
    def create_appointment(cls, appointment: Appointment) -> None:
        connection = Connection.create()

        appointment_dict = appointment_schema.dump(appointment)
        query = CREATE_APPOINTMENT.format(**appointment_dict)

        cursor = Connection.execute(connection, query)
        connection.commit()

        if cursor:
            cursor.close()

    @classmethod
    def is_appointment_taken(cls, appointment: Appointment) -> bool:
        connection = Connection.create()

        appointment_dict = appointment_schema.dump(appointment)
        query = IS_APPOINTMENT_TAKEN.format(**appointment_dict)

        cursor = Connection.execute(connection, query)
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
    def get_active_appointments(cls, patient_id: str) -> list[Appointment]:
        query = ACTIVE_APPOINTMENTS.format(patient_id=patient_id)
        return cls.__get_appointments(query)

    @classmethod
    def get_past_appointments(cls, patient_id: str) -> list[Appointment]:
        query = PAST_APPOINTMENTS.format(patient_id=patient_id)
        return cls.__get_appointments(query)

    @classmethod
    def __get_appointments(cls, query: str) -> list[Appointment]:
        connection = Connection.create()
        cursor = Connection.execute(connection, query)

        appointments = []
        if cursor:
            for row in cursor:
                formatted_date = StringHandler.select_first_element_of(
                    str(row[0]))

                appointment = Appointment(id=row[11], date=formatted_date, time=row[1],
                                          profession_id=row[2], profession_name=row[3],
                                          doctor_id=row[4], doctor_name=row[5],
                                          doctor_surname=row[6], patient_name=row[7],
                                          patient_surname=row[8], patient_father=row[9],
                                          patient_birthday=row[10])
                appointments.append(appointment)

            cursor.close()

        return appointments


    @classmethod
    def cancel_appointment(cls, appointment_id: str) -> None:
        connection = Connection.create()

        query = CANCEL_APPOINTMENT.format(appointment_id=appointment_id)
        cursor = Connection.execute(connection, query)
        connection.commit()

        if cursor:
            cursor.close()

    
    @classmethod
    def is_appointment_exist(cls, appointment_id: str) -> bool:
        connection = Connection.create()
        query = IS_APPOINTMENT_EXIST.format(appointment_id=appointment_id)

        cursor = Connection.execute(connection, query)
        row = cursor.fetchone()
    

        if row:
            return True
        return False
