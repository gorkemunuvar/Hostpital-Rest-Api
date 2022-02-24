from core.enums import Lang
from models.news import News
from core.utils.database.database import Connection
from core.utils.database.queries.ru.news import NEWS
from core.utils.database.queries.kk.news import KK_NEWS
from core.utils.image_handler import ImageHandler
from core.utils.string_handler import StringHandler
from core.utils.pagination_handler import get_start_and_end

class NewsService():
    @staticmethod
    def get_news(page: int, lang: Lang = None) -> list[News]:
        start, end = get_start_and_end(page)
        query = KK_NEWS if lang is Lang.KK else NEWS
        query = query.format(start=start, end=end)

        connection = Connection.create()
        cursor = Connection.execute(connection, query)

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
