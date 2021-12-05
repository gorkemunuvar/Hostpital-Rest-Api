from flask import request, abort
from flask_restful import Resource

from services.news import NewsService
from schemas.news import NewsSchema
from schemas.pagination import PaginationSchema


pagination_schema = PaginationSchema()
all_news_schema = NewsSchema(many=True)


class News(Resource):
    @classmethod
    def get(self):
        # Defaults
        page = 1
        per_page = 5

        query_params = request.args
        errors = pagination_schema.validate(query_params)

        if errors:
            abort(400, str(errors))

        if query_params.__contains__('page'):
            page = int(query_params['page'])

        if query_params.__contains__('per_page'):
            per_page = int(query_params['per_page'])

        news = NewsService.get_news(page=page, per_page=per_page)
        news_dict = all_news_schema.dump(news)
        
        return {'news': news_dict}, 200
