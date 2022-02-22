from core.utils.database.database import Connection
from models.polyclinic import Polyclinic
from core.utils.database.queries.ru.polyclinic import POLYCLINICS, SEARCH_POLYCLINICS
from core.utils.image_handler import ImageHandler


class PolyclinicService():
    @staticmethod
    def get_polyclinics() -> list[Polyclinic]:
        connection = Connection.create()
        cursor = Connection.execute(connection, POLYCLINICS)

        polyclinics = []
        if cursor:
            for row in cursor:
                image_base64 = ''
                lob_image = row[3]

                if lob_image:
                    image_base64 = ImageHandler.convert_lob_to_base64_str(
                        lob_image)

                description = row[2]
                if not description:
                    description = '-'

                polyclinic = Polyclinic(id=row[0], title=row[1],
                                        description=description,
                                        image_base64 = image_base64)
                polyclinics.append(polyclinic)

            cursor.close()

        return polyclinics

    @staticmethod
    def search_polyclinics(search_string: str) -> list[Polyclinic]:
        connection = Connection.create()
        cursor = Connection.execute(
            connection, SEARCH_POLYCLINICS.format(search_string=search_string)
        )

        polyclinics = []
        if cursor:
            for row in cursor:
                image_base64 = ''
                lob_image = row[3]

                if lob_image:
                    image_base64 = ImageHandler.convert_lob_to_base64_str(
                        lob_image)

                description = row[2]
                if not description:
                    description = '-'

                polyclinic = Polyclinic(id=row[0], title=row[1],
                                        description=description,
                                        image_base64=image_base64)
                polyclinics.append(polyclinic)

            cursor.close()

        return polyclinics
