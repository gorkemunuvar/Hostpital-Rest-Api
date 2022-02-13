from typing import Union
from models.patient import Patient
from .database import Connection
from utils.queries import CHECK_PATIENT, CREATE_PATIENT_ID, CREATE_PATIENT, GET_PATIENT
from utils.string_handler import StringHandler

class PatientService():
    @staticmethod
    def is_patient_exist(name: str, surname: str, birthday: str) -> bool:
        connection = Connection.create()
        query = CHECK_PATIENT.format(name=name, surname=surname, birthday=birthday)

        cursor = Connection.execute(connection, query)
        
        if cursor:
            row = cursor.fetchone()
            cursor.close()

        if row:
            return True
        return False

    @staticmethod
    def create_patient_id() -> str:
        connection = Connection.create()
        cursor = connection.cursor()

        if cursor:
            patient_id = cursor.callfunc(CREATE_PATIENT_ID, str)
            cursor.close()

        return patient_id

    @staticmethod
    def create_patient(patient_id: str, name: str, surname: str,
                       birthday: str, phone_number: str) -> None:
        connection = Connection.create()
        cursor = connection.cursor()

        query = CREATE_PATIENT.format(patient_id=patient_id, name=name,
                                      surname=surname, birthday=birthday,
                                      phone_number=phone_number)

        cursor = Connection.execute(connection, query)
        connection.commit()

        if cursor:    
            cursor.close()

    @staticmethod
    def get_patient(name: str, surname: str, birthday: str,
                    phone_number: str) -> Union[Patient, None]:
        connection = Connection.create()
        cursor = connection.cursor()

        query = GET_PATIENT.format(name=name, surname=surname,
                                   birthday=birthday, phone_number=phone_number)

        cursor = Connection.execute(connection, query)

        if cursor:
            row = cursor.fetchone()

            if row:
                patient = Patient(id=row[0], name=row[1], surname=row[2],
                                birthday=row[4], phone_number=row[5])
                return patient

            cursor.close()

        return None
