from utils.database.database import Connection
from utils.database.queries.available_date import (AVAILABLE_DATES_BY_DOCTOR_ID,
                                    AVAILABLE_DATES_WITHOUT_DOCTOR)


class AvailableAppoinmentDateService():
    @classmethod
    def get_avaiable_appoinment_dates_by_doctor_id(cls, id: str) -> list[str]:
        query = AVAILABLE_DATES_BY_DOCTOR_ID.format(doctor_id=id)
        dates = cls.__get_avaiable_appoinment_dates(query)
        return dates

    @classmethod
    def get_available_appointment_dates_by_profession(cls) -> list[str]:
        query = AVAILABLE_DATES_WITHOUT_DOCTOR
        dates = cls.__get_avaiable_appoinment_dates(query)
        return dates

    @classmethod
    def __get_avaiable_appoinment_dates(cls, query: str) -> list[str]:
        connection = Connection.create()
        cursor = Connection.execute(connection, query)

        dates = []
        if cursor:
            for row in cursor:
                # 2021-11-14 00:00:00
                date = str(row[0]).split()[0]
                dates.append(date)

            cursor.close()

        return dates
