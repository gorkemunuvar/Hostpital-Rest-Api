from .database import Connection
from utils.queries import GET_AVAILABLE_APPOINTMENT_DATES

connection = Connection.create()


class AvailableAppoinmentDateService():
    @staticmethod
    def get_avaiable_appoinment_dates_by_doctor_id(id: str) -> list[str]:
        query = GET_AVAILABLE_APPOINTMENT_DATES.format(doctor_id=id)
        cursor = Connection.execute(connection, query)

        dates = []
        for row in cursor:
            # 2021-11-14 00:00:00
            date = str(row[0]).split()[0]
            dates.append(date)

        return dates
