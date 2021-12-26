from .database import Connection
from models.profession import Profession
from schemas.profession import ProfessionSchema

connection = Connection.create()

professions_schema = ProfessionSchema(many=True)


class ProfessionService():
    @staticmethod
    def get_professions_by_polyclinic_id(id: str) -> list[Profession]:
        query = "select KABINET,ISIM,SINIFI from ng_his_glzr WHERE PROFS = :PROFS"
        parameters = {':PROFS': id}

        print('BİR')
        cursor = Connection.execute(connection, query, parameters)
        print('İKİ')


        professions = []
        for row in cursor:
            profession = Profession(id=row[0], name=row[1])
            professions.append(profession)

        return professions
