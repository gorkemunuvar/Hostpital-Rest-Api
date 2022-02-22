from utils.database.database import Connection
from models.profession import Profession
from utils.database.queries.ru.profession import PROFESSIONS_BY_POLYCLINIC_ID


class ProfessionService():
    @staticmethod
    def get_professions_by_polyclinic_id(id: str) -> list[Profession]:
        connection = Connection.create()
        query = PROFESSIONS_BY_POLYCLINIC_ID.format(polyclinic_id=id)

        cursor = Connection.execute(connection, query)

        professions = []
        if cursor:
            for row in cursor:
                profession = Profession(id=row[0], name=row[1], type=row[2])
                professions.append(profession)

            cursor.close()

        return professions
