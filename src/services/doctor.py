

from .database import Connection
from models.doctor import Doctor
from schemas.doctor import DoctorSchema
from utils.queries import (ALL_DOCTORS, DOCTOR_BY_ID,
                           DOCTORS_BY_POLYCLINIC_ID, DOCTORS_BY_PROFESSION_ID)


connection = Connection.create()

doctor_schema = DoctorSchema()
doctors_schema = DoctorSchema(many=True)


class DoctorService():
    @staticmethod
    def get_all_doctors(page: int, per_page: int) -> list[Doctor]:
        cursor = Connection.execute(connection, ALL_DOCTORS)

        doctors = []
        for row in cursor:
            doctor = Doctor(id=row[0], surname=row[1],
                            name=row[2], father=row[3],
                            description=row[4])

            doctors.append(doctor)

        return doctors

    @staticmethod
    def get_doctor_by_id(doctor_id: str) -> Doctor:
        cursor = Connection.execute(connection, DOCTOR_BY_ID)

        doctor = Doctor()

        for row in cursor:


            doctor = Doctor(id=row[0], surname=row[1], name=row[2], father=row[3],
                            description=row[4], profession=row[6], education=row[7],
                            experience=row[8], achievements=row[9])

            break

        return doctor

    @staticmethod
    def get_doctors_by_polyclinic_id(id: str):
        query = DOCTORS_BY_POLYCLINIC_ID.format(polyclinic_id=id)
        cursor = Connection.execute(connection, query)

        doctors = []
        for row in cursor:
            doctor = Doctor(id=row[0], surname=row[1], name=row[2],
                            father=row[3], description=row[4], polyclinic_id=row[6])
            doctors.append(doctor)

        return doctors

    @staticmethod
    def get_doctors_by_profession_id(id: str):
        query = DOCTORS_BY_PROFESSION_ID.format(profession_id=id)
        cursor = Connection.execute(connection, query)

        doctors = []
        for row in cursor:
            doctor = Doctor(id=row[0], surname=row[1], name=row[2])
            doctors.append(doctor)

        return doctors

    @staticmethod
    def search_doctor(search_text: str) -> list[Doctor]:
        pass
