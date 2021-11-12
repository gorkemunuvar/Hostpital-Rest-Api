from flask_restful import Resource

from test_data.hospitals import test_hospitals_data

class Hospitals(Resource):
    @classmethod
    def get(self):

        return {'hospitals': test_hospitals_data}
