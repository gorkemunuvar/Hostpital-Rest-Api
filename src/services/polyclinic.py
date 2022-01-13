from .database import Connection
from models.polyclinic import Polyclinic
from utils.queries import POLYCLINICS, SEARCH_POLYCLINICS

connection = Connection.create()

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
    def search_polyclinics(search_string: str) -> list[Polyclinic]:
        cursor = Connection.execute(
            connection, SEARCH_POLYCLINICS.format(search_string=search_string)
        )

        polyclinics = []
        for row in cursor:
            description = row[2]
            if not description:
                description = '-'

            polyclinic = Polyclinic(id=row[0], title=row[1],
                                    description=description)
            polyclinics.append(polyclinic)

        return polyclinics
