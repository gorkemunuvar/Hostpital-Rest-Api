from schemas import polyclinic
from .database import Connection
from models.profession import Profession
from schemas.profession import ProfessionSchema
from utils.queries import PROFESSIONS_BY_POLYCLINIC_ID

connection = Connection.create()

professions_schema = ProfessionSchema(many=True)


class ProfessionService():
    @staticmethod
    def get_professions_by_polyclinic_id(id: str) -> list[Profession]:
        query = PROFESSIONS_BY_POLYCLINIC_ID.format(polyclinic_id=id)

        cursor = Connection.execute(connection, query)

        professions = []
        for row in cursor:
            profession = Profession(id=row[0], name=row[1])
            professions.append(profession)

        return professions
