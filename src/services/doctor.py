from core.utils.database.database import Connection
from models.doctor import Doctor
from core.utils.image_handler import ImageHandler
from core.utils.pagination_handler import get_start_and_end
from core.utils.database.queries.ru.doctor import (ALL_DOCTORS, DOCTOR_BY_ID,
                            DOCTORS_BY_POLYCLINIC_ID, DOCTORS_BY_PROFESSION_ID,
                            SEARCH_DOCTORS)


class DoctorService():
    @staticmethod
    def get_all_doctors(page: int) -> list[Doctor]:
        start, end = get_start_and_end(page)
        print(f'START: {start} - END: {end}')

        connection = Connection.create()
        query = ALL_DOCTORS.format(start=start, end=end)
        cursor = Connection.execute(connection, query)

        doctors = []
        if cursor:
            for row in cursor:
                doctor_image_base64 = ''
                lob_image = row[5]

                if lob_image:
                    doctor_image_base64 = ImageHandler.convert_lob_to_base64_str(
                        lob_image)

                doctor = Doctor(id=row[0], surname=row[1],
                                name=row[2], father=row[3],
                                description=row[4], image_base64=doctor_image_base64,
                                profession=row[6], education=row[7],
                                experience=row[8], achievements=row[9])

                doctors.append(doctor)

            cursor.close()

        print(f'DOCTORS LENGTH: {len(doctors)}')



        return doctors

    @staticmethod
    def get_doctor_by_id(id: str) -> Doctor:
        connection = Connection.create()

        query = DOCTOR_BY_ID.format(id=id)
        cursor = Connection.execute(connection, query)

        doctor = Doctor()
        if cursor:
            for row in cursor:
                doctor = Doctor(id=row[0], surname=row[1], name=row[2], father=row[3],
                                description=row[4], profession=row[6], education=row[7],
                                experience=row[8], achievements=row[9])
                break

            cursor.close()

        return doctor

    @staticmethod
    def get_doctors_by_polyclinic_id(id: str):
        connection = Connection.create()
        query = DOCTORS_BY_POLYCLINIC_ID.format(polyclinic_id=id)
        cursor = Connection.execute(connection, query)

        doctors = []
        if cursor:
            for row in cursor:
                doctor_image_base64 = ''
                lob_image = row[9]

                if lob_image:
                    doctor_image_base64 = ImageHandler.convert_lob_to_base64_str(
                        lob_image)

                doctor = Doctor(id=row[0], surname=row[1], name=row[2],
                                father=row[3], description=row[4], profession=row[5],
                                education=row[6], experience=row[7], achievements=row[8],
                                image_base64=doctor_image_base64)

                doctors.append(doctor)
                
            cursor.close()

        return doctors

    @staticmethod
    def get_doctors_by_profession_id(id: str):
        connection = Connection.create()
        query = DOCTORS_BY_PROFESSION_ID.format(profession_id=id)
        cursor = Connection.execute(connection, query)

        doctors = []
        if cursor:
            for row in cursor:
                doctor = Doctor(id=row[0], surname=row[1], name=row[2])
                doctors.append(doctor)

            cursor.close()

        return doctors

    @staticmethod
    def search_doctors(search_string: str) -> list[Doctor]:
        connection = Connection.create()
        cursor = Connection.execute(
            connection, SEARCH_DOCTORS.format(search_string=search_string)
        )

        doctors = []
        if cursor:
            for row in cursor:
                doctor_image_base64 = ''
                lob_image = row[5]

                if lob_image:
                    doctor_image_base64 = ImageHandler.convert_lob_to_base64_str(
                        lob_image)

                doctor = Doctor(id=row[0], surname=row[1],
                                name=row[2], father=row[3],
                                description=row[4], image_base64=doctor_image_base64,
                                profession=row[6], education=row[7],
                                experience=row[8], achievements=row[9])

                doctors.append(doctor)

            cursor.close()

        return doctors
