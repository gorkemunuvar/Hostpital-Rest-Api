import datetime

from utils.database.database import Connection
from utils.database.queries.ru.available_hour import (AVAILABLE_HOURS,
                                                   AVAILABLE_HOUR_REQUIREMENTS_BY_DOCTOR_ID,
                                                   AVAILABLE_HOUR_REQUIREMENTS_BY_PROFESSION)


class AvailableHourService():
    @staticmethod
    def get_avaiable_hours(selected_date: str, id: str = None) -> list[str]:
        """selected_date format <yyyy/mm/dd>"""

        if id:
            query_requirements = get_query_requirements(selected_date, id)
        else:
            query_requirements = get_query_requirements(selected_date)

        if not query_requirements:
            return []

        query = AVAILABLE_HOURS.format(
            appointment_date=query_requirements['appointment_date'],
            beginning_time=query_requirements['beginning_time'],
            ending_time=query_requirements['ending_time'],
            profession_id=query_requirements['profession_id'],
            time_interval=query_requirements['time_interval']
        )

        connection = Connection.create()
        cursor = Connection.execute(connection, query)

        available_hours = []
        if cursor:
            for row in cursor:
                available_hours.append(str(row[1]))

            cursor.close()

        return available_hours


def get_query_requirements(selected_date: str, doctor_id: str = None) -> dict:
    """selected_date format <yyyy/mm/dd>"""

    query_for_requirements = ''
    if doctor_id:
        query_for_requirements = AVAILABLE_HOUR_REQUIREMENTS_BY_DOCTOR_ID.format(
            doctor_id=doctor_id)
    else:
        query_for_requirements = AVAILABLE_HOUR_REQUIREMENTS_BY_PROFESSION

    connection = Connection.create()
    cursor = Connection.execute(connection, query_for_requirements)

    query_requirements = {}
    if cursor:
        for row in cursor:
            # 2021-12-29 21:04:08 (db date format)
            date = str(row[0]).split()[0]

            # returns 2021-12-29
            formatted_date = format_date(selected_date)

            if formatted_date == date:
                beginning_time = str(row[2])
                ending_time = str(row[3])
                profession_id = row[4]
                time_interval = row[7]

                query_requirements = {
                    'appointment_date': date,
                    'beginning_time': beginning_time,
                    'ending_time': ending_time,
                    'profession_id': profession_id,
                    'time_interval': time_interval
                }

                break

        cursor.close()

    return query_requirements


def format_date(date: str) -> str:
    """Returns <yyyy-mm-dd> for given <yyyy/mm/dd> format."""
    return datetime.datetime.strptime(date, "%Y/%m/%d").strftime("%Y-%m-%d")
