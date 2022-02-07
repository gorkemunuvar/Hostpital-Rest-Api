import datetime

from .database import Connection
from utils.queries import (AVAILABLE_APPOINTMENT_TIMES,
                           AVAILABLE_APPOINTMENT_TIME_REQUIREMENTS)

connection = Connection.create()


class AvailableAppoinmentTimeService():
    @staticmethod
    def get_avaiable_appoinment_times_by_doctor_id_and_date(id: str, selected_date: str) -> list[str]:
        """selected_date format <yyyy/mm/dd>"""

        query_requirements = get_query_requirements(id, selected_date)

        if not query_requirements:
            return []

        query = AVAILABLE_APPOINTMENT_TIMES.format(
            appointment_date=query_requirements['appointment_date'],
            beginning_time=query_requirements['beginning_time'],
            ending_time=query_requirements['ending_time'],
            profession_id=query_requirements['profession_id'],
            time_interval=query_requirements['time_interval']
        )
        cursor = Connection.execute(connection, query)

        available_times = []
        if cursor:
            for row in cursor:
                available_times.append(str(row[1]))

            cursor.close()

        return available_times


def get_query_requirements(doctor_id: str, selected_date: str) -> dict:
    """selected_date format <yyyy/mm/dd>"""
    query_for_requirements = AVAILABLE_APPOINTMENT_TIME_REQUIREMENTS.format(
        doctor_id=doctor_id)

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
