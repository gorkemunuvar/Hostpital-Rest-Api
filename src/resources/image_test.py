import imp
from flask_restful import Resource
from services.database import Connection
from utils.queries import DOCTOR_BY_ID

connection = Connection.create()

class ImageTest(Resource):
    @classmethod
    def get(cls):
        cursor = Connection.execute(connection, DOCTOR_BY_ID)

        for row in cursor:
            print(row[1])
            print(row[2])
            image_blob = row[5]
            blob = image_blob.read()

            


            
            print('blob type')
            print(type(blob))

            return {'message': 'image data'}, 200

