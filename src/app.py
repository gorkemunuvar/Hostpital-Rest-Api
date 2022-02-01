import routes

from flask import Flask
from flask.blueprints import Blueprint

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey321'


def init_bluprints():
    for blueprint in vars(routes).values():
        if isinstance(blueprint, Blueprint):
            app.register_blueprint(blueprint)


if __name__ == '__main__':
    init_bluprints()

    app.run(debug=True)
