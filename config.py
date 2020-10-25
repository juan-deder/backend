import os


class Config:
    SECRET_KEY = 'veryScreteKey'
    SQLACHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:1234@postgres:5432/postgres'


class DevelopmentConfig(Config):
    path = os.path.dirname(os.path.abspath(__name__))
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{path}/database/db.sqlite'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://:memory:'


config = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig
}
