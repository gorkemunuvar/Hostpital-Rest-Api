from .database import Database
from models.expertise import Expertise
from schemas.expertise import ExpertiseSchema

expertises_schema = ExpertiseSchema(many=True)

connection = Database.connect()


class ExpertiseService():
    @staticmethod
    def get_expertises_by_polyclinic_id(id: str) -> list[Expertise]:
        cursor = connection.cursor()
        cursor.execute(
            f"select KABINET,ISIM,SINIFI from ng_his_glzr WHERE PROFS='{id}'"
        )

        expertises = []
        for row in cursor:
            expertise = Expertise(id=row[0], name=row[1])
            expertises.append(expertise)

        return expertises
