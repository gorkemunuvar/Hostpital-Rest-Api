import json
import cx_Oracle


class Hospital():
    def __init__(self) -> None:
        self.id = ''
        self.name = ''

    def fetch_hospitals(cls):
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
            hospitals.append({
                'id': row[0],
                'name': row[1]
            })
