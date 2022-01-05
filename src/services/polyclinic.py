from .database import Connection
from models.polyclinic import Polyclinic
from schemas.polyclinic import PolyclinicSchema
from utils.queries import POLYCLINICS

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

            polyclinic = Polyclinic(id=row[0], title=row[1],
                                    description=description)
            polyclinics.append(polyclinic)

        return polyclinics

    @staticmethod
    def search_polyclinics(search_text: str) -> list[Polyclinic]:
        pass
