from .database import Connection
from models.polyclinic import Polyclinic
from schemas.polyclinic import PolyclinicSchema
from test_data.polyclinics import test_polyclinics_data
from utils.queries import POLYCLINICS, POLYCLINIC_BY_ID

connection = Connection.create()

polyclinic_schema = PolyclinicSchema()
polyclinics_schema = PolyclinicSchema(many=True)


class PolyclinicService():
    @staticmethod
    def get_polyclinics() -> list[Polyclinic]:
        cursor = Connection.execute(connection, POLYCLINICS)

        polyclinics = []
        for row in cursor:
            description = row[2]
            if not description:
                description = '-'

            polyclinic = Polyclinic(
                id=row[0], title=row[1], description=description)
            polyclinics.append(polyclinic)

        return polyclinics

    @staticmethod
    def get_polyclinic_by_id() -> Polyclinic:
    #def get_polyclinic_by_id(polyclinic_id: str) -> Polyclinic:
        cursor = Connection.execute(connection, POLYCLINIC_BY_ID)

        doctor_list = []
        for row in cursor:
            new_dict = {
                'doctor_id': row[0],
                'soyad': row[1],
                'ad': row[2],
                'polyclinic_id': row[4],
                'doctor_description': row[5]
            }

            doctor_list.append(new_dict)

        return doctor_list


        # polyclinic_dict = test_polyclinics_data[int(polyclinic_id) - 1]
        # polyclinic = polyclinic_schema.load(polyclinic_dict)

        # return polyclinic

    @staticmethod
    def get_polyclinics_by_hospital_id(id: str) -> list[Polyclinic]:
        polyclinics = []

        for item in test_polyclinics_data:
            if id == item['hospital_id']:
                polyclinic = Polyclinic(id=item['id'],
                                        hospital_id=item['hospital_id'],
                                        title=item['title'])

                polyclinics.append(polyclinic)

        return polyclinics

    @staticmethod
    def search_polyclinics(search_text: str) -> list[Polyclinic]:
        polyclinics = []

        for item in test_polyclinics_data:
            if search_text.lower() in item['title'].lower():
                polyclinic = polyclinic_schema.load(item)
                polyclinics.append(polyclinic)

        return polyclinics
