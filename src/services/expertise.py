from .database import Connection
from models.expertise import Expertise
from schemas.expertise import ExpertiseSchema

connection = Connection.create()

expertises_schema = ExpertiseSchema(many=True)


class ExpertiseService():
    @staticmethod
    def get_expertises_by_polyclinic_id(id: str) -> list[Expertise]:
        query = "select KABINET,ISIM,SINIFI from ng_his_glzr WHERE PROFS = :PROFS"
        parameters = {':PROFS', id} 

        cursor = Connection.execute(connection, query, parameters)

        expertises = []
        for row in cursor:
            expertise = Expertise(id=row[0], name=row[1])
            expertises.append(expertise)

        return expertises
