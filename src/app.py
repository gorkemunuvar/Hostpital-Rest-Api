import routes

from flask import Flask
from flask.blueprints import Blueprint

from core.utils.config import DevelopmentConfig

configs = DevelopmentConfig()

app = Flask(__name__)
app.config['SECRET_KEY'] = configs.APP_SECRET_KEY


def init_bluprints():
    for blueprint in vars(routes).values():
        if isinstance(blueprint, Blueprint):
            app.register_blueprint(blueprint)


if __name__ == '__main__':
    init_bluprints()

    app.run(debug=True)
