import routes

from flask import Flask
from flask.blueprints import Blueprint

from services.database import Connection
from services.patient import PatientService

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey321'

def init_bluprints():
    for blueprint in vars(routes).values():
        if isinstance(blueprint, Blueprint):
            app.register_blueprint(blueprint)

def login_logic():
    is_patient_exist = PatientService.is_patient_exist()

    if not is_patient_exist:
        patient_id = PatientService.create_patient_id()
        PatientService.create_patient(str(patient_id))
        print('Hasta Oluşturuldu.')
    else:
        print('Hasta zaten kayıtlı.')



if __name__ == '__main__':
    init_bluprints()
    
    login_logic()

    app.run(debug=True)
