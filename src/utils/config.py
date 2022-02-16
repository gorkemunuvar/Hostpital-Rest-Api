import os


class Config(object):
    DEBUG = True
    ENV = 'development'
    APP_SECRET_KEY = os.environ.get('APP_SECRET_KEY')

    DB_URL = os.environ.get('DB_URL')
    DB_PORT = os.environ.get('DB_PORT')
    DB_SERVICE_NAME = os.environ.get('DB_SERVICE_NAME')
    DB_USERNAME = os.environ.get('DB_USERNAME')
    DB_PASSWORD = os.environ.get('DB_PASSWORD')


class ProductionConfig(Config):
    DEBUG = False
    ENV = 'production'


class DevelopmentConfig(Config):
    pass
