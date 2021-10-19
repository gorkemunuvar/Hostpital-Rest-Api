from flask_restful import Resource

from test_data.polyclinics import test_polyclinics_data


class Polyclinics(Resource):
    @classmethod
    def get(cls):
        return {'polyclinics': test_polyclinics_data}, 200
