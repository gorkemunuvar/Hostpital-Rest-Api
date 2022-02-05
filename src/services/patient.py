from typing import Union
from unicodedata import name
from models.patient import Patient
from .database import Connection
from utils.queries import CHECK_PATIENT, CREATE_PATIENT_ID, CREATE_PATIENT, GET_PATIENT
from utils.string_handler import StringHandler

connection = Connection.create()


class PatientService():
    @staticmethod
    def is_patient_exist() -> bool:
        cursor = Connection.execute(connection, CHECK_PATIENT)
        row = cursor.fetchone()

        if cursor:
            cursor.close()

        if row:
            return True
        return False

    @staticmethod
    def create_patient_id() -> str:
        connection = Connection.create()
        cursor = connection.cursor()

        patient_id = cursor.callfunc(CREATE_PATIENT_ID, str)

        if cursor:
            cursor.close()

        return patient_id

    @staticmethod
    def create_patient(patient_id: str) -> None:
        connection = Connection.create()
        cursor = connection.cursor()

        cursor = Connection.execute(
            connection, CREATE_PATIENT.format(patient_id=patient_id))

        connection.commit()

        if cursor:
            cursor.close()

    @staticmethod
    def get_patient() -> Union[Patient, None]:
        connection = Connection.create()
        cursor = connection.cursor()

        cursor = Connection.execute(connection, GET_PATIENT)
        row = cursor.fetchone()

        if row:
            patient = Patient(id=row[0], name=row[1], surname=row[2],
                              father=row[3], birthday=row[4], phone_number=row[5])
            return patient

        if cursor:
            cursor.close()

        return None
