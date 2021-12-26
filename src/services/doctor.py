from .database import Connection
from models.doctor import Doctor
from test_data.doctors import test_doctors_data
from schemas.doctor import DoctorSchema
from utils.queries import DOCTORS_BY_PROFESSION_ID

connection = Connection.create()

doctor_schema = DoctorSchema()
doctors_schema = DoctorSchema(many=True)


class DoctorService():
    @staticmethod
    def get_doctors(page: int, per_page: int) -> list[Doctor]:
        start = page * per_page - per_page
        end = page * per_page

        doctors = doctors_schema.load(test_doctors_data[start:end])

        return doctors

    @staticmethod
    def get_doctor_by_id(doctor_id: str) -> Doctor:
        doctor = Doctor()

        for item in test_doctors_data:
            if item['id'] == doctor_id:
                doctor = doctor_schema.load(item)
                break

        return doctor

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
        doctors = []
        for item in test_doctors_data:
            doctor_fullname = item['name'] + ' ' + item['surname']

            if search_text.lower() in doctor_fullname.lower():
                doctor_dict = doctor_schema.load(item)
                doctors.append(doctor_dict)

        return doctors
