from flask import request
from flask_restful import Resource

from core.utils.get_lang import get_lang
from services.news import NewsService
from core.utils.schemas.news import NewsSchema
from core.utils.schemas.pagination import PaginationSchema


pagination_schema = PaginationSchema()
all_news_schema = NewsSchema(many=True)


class News(Resource):
    @classmethod
    def get(self):
        page = 1
        per_page = 5

        try:
            query_params = request.args
            lang = get_lang(query_params)
    
            if query_params.__contains__('page'):
                page = int(query_params['page'])

            if query_params.__contains__('per_page'):
                per_page = int(query_params['per_page'])

            news_list = NewsService.get_news(lang=lang)
            news_dict = all_news_schema.dump(news_list)

            return {'news': news_dict}, 200
        except Exception as error:
            print(error)
            return {'message': f'Something went wrong. ({error})'.format(error=error)}, 500



