from models.hospital import Hospital
from .database import DbConnectionSingleton

connection = DbConnectionSingleton.connect()


class HospitalService():
    @staticmethod
    def get_hospitals() -> list[Hospital]:
        cursor = connection.cursor()
        cursor.execute("""select DBKOD,DBAD from NG_HIS_LNKDBS t""")

        hospitals = []
        for row in cursor:
            hospital = Hospital(id=row[0], name=row[1])
            hospitals.append(hospital)

        return hospitals
