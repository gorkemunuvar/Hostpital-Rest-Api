from utils.database import Connection
from models.polyclinic import Polyclinic
from queries.polyclinic import POLYCLINICS, SEARCH_POLYCLINICS


class PolyclinicService():
    @staticmethod
    def get_polyclinics() -> list[Polyclinic]:
        connection = Connection.create()
        cursor = Connection.execute(connection, POLYCLINICS)

        polyclinics = []
        if cursor:
            for row in cursor:
                description = row[2]
                if not description:
                    description = '-'

                polyclinic = Polyclinic(id=row[0], title=row[1],
                                        description=description)
                polyclinics.append(polyclinic)

            cursor.close()

        return polyclinics

    @staticmethod
    def search_polyclinics(search_string: str) -> list[Polyclinic]:
        connection = Connection.create()
        cursor = Connection.execute(
            connection, SEARCH_POLYCLINICS.format(search_string=search_string)
        )

        polyclinics = []
        if cursor:
            for row in cursor:
                description = row[2]
                if not description:
                    description = '-'

                polyclinic = Polyclinic(id=row[0], title=row[1],
                                        description=description)
                polyclinics.append(polyclinic)

            cursor.close()

        return polyclinics
