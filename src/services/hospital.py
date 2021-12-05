import cx_Oracle

from models.hospital import Hospital


class HospitalService():
    @staticmethod
    def get_hospitals() -> list[Hospital]:
        connection = cx_Oracle.connect(
            user="sys",
            password="123",
            dsn="localhost/orcl",
            mode=cx_Oracle.SYSDBA
        )

        cursor = connection.cursor()
        cursor.execute("""select DBKOD,DBAD from NG_HIS_LNKDBS t""")

        hospitals = []
        for row in cursor:
            hospital = Hospital(id=row[0], name=row[1])
            hospitals.append(hospital)

        return hospitals
