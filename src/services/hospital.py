from .database import Connection
from models.hospital import Hospital
from utils.queries import HOSPITALS

connection = Connection.create()


class HospitalService():
    @staticmethod
    def get_hospitals() -> list[Hospital]:
        cursor = Connection.execute(connection, HOSPITALS)
        
        hospitals = []
        for row in cursor:
            hospital = Hospital(id=row[0], name=row[1])
            hospitals.append(hospital)

        return hospitals
