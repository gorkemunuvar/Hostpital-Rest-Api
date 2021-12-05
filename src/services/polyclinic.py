import json

from models.polyclinic import Polyclinic
from schemas.polyclinic import PolyclinicSchema
from test_data.polyclinics import test_polyclinics_data

polyclinic_schmea = PolyclinicSchema()
polyclinics_schmea = PolyclinicSchema(many=True)


class PolyclinicService():
    @staticmethod
    def get_polyclinics() -> list[Polyclinic]:
        polyclinics = polyclinics_schmea.load(test_polyclinics_data)

        return polyclinics

    @staticmethod
    def get_polyclinic_by_id(polyclinic_id: str) -> Polyclinic:
        polyclinic_dict = test_polyclinics_data[int(polyclinic_id) - 1]
        polyclinic = polyclinic_schmea.load(polyclinic_dict)

        return polyclinic

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
                polyclinic = polyclinic_schmea.load(item)
                polyclinics.append(polyclinic)

        return polyclinics
