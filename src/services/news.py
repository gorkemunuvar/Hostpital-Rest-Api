from models.news import News
from utils.database import Connection
from utils.queries import NEWS
from utils.image_handler import ImageHandler
from utils.string_handler import StringHandler


class NewsService():
    @staticmethod
    def get_news() -> list[News]:
        connection = Connection.create()
        cursor = Connection.execute(connection, NEWS)

        news_list = []
        if cursor:
            for row in cursor:
                doctor_image_base64 = ''
                lob_image = row[4]

                if lob_image:
                    doctor_image_base64 = ImageHandler.convert_lob_to_base64_str(
                        lob_image)

                date = StringHandler.select_first_element_of(str(row[1]))
                news = News(id=row[0], date=date,
                            title=row[2], description=row[3],
                            image_base64=doctor_image_base64)

                news_list.append(news)

            cursor.close()

        return news_list
