import routes

from flask import Flask
from flask.blueprints import Blueprint

from services.database import Connection

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey321'


def init_bluprints():
    for blueprint in vars(routes).values():
        if isinstance(blueprint, Blueprint):
            app.register_blueprint(blueprint)


def call_function():
    connection = Connection.create()
    cursor = connection.cursor()
    patient_id = cursor.callfunc('PASTNOAL', str)
    
    print('-----')
    print('Function called succesfully')
    print(patient_id)

if __name__ == '__main__':

    init_bluprints()
    call_function()

    app.run(debug=True)
