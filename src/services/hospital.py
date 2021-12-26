from models.hospital import Hospital
from .database import Connection

connection = Connection.create()


class HospitalService():
    @staticmethod
    def get_hospitals() -> list[Hospital]:
        query = 'select DBKOD,DBAD from NG_HIS_LNKDBS t'

        cursor = Connection.execute(connection, query)

        hospitals = []
        for row in cursor:
            hospital = Hospital(id=row[0], name=row[1])
            hospitals.append(hospital)

        return hospitals
