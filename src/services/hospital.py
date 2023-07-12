from core.utils.database.database import Connection
from models.hospital import Hospital
from core.utils.database.queries.ru.hospital import HOSPITALS


class HospitalService():
    @staticmethod
    def get_hospitals() -> list[Hospital]:
        connection = Connection.create()
        cursor = Connection.execute(connection, HOSPITALS)

        hospitals = []
        if cursor:
            for row in cursor:
                hospital = Hospital(id=row[0], name=row[1])
                hospitals.append(hospital)

            cursor.close()

        return hospitals
