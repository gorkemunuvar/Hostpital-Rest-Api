from models.patient import Patient
from .database import Connection
from utils.queries import CHECK_PATIENT, CREATE_PATIENT_ID, CREATE_PATIENT
from utils.string_handler import StringHandler

connection = Connection.create()


class PatientService():
    @staticmethod
    def is_patient_exist() -> bool:
        cursor = Connection.execute(connection, CHECK_PATIENT)
        row = cursor.fetchone()
        cursor.close()

        if row:
            return True
        return False

    @staticmethod
    def create_patient_id() -> str:
        connection = Connection.create()
        cursor = connection.cursor()

        patient_id = cursor.callfunc(CREATE_PATIENT_ID, str)
        cursor.close()

        return patient_id

    @staticmethod
    def create_patient(patient_id: str) -> None:
        connection = Connection.create()
        cursor = connection.cursor()

        cursor = Connection.execute(
            connection, CREATE_PATIENT.format(patient_id=patient_id))
        cursor.close()
