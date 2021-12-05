from models.news import News
from schemas.news import NewsSchema
from schemas.news import NewsSchema
from test_data.news import test_news_data

all_news_schema = NewsSchema(many=True)


class NewsService():
    @staticmethod
    def get_news(page: int, per_page: int) -> list[News]:
        start = page * per_page - per_page
        end = page * per_page

        news = all_news_schema.load(test_news_data[start:end])
        
        return news
