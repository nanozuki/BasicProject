import os
import private_config

base_dir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = private_config.SECRET_KEY
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    @staticmethod
    def init_app(app):
        pass


class DevelopConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = ''


class TestConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = ''


class ProductionConfig(Config):
    DEBUG = False


config = {
    "develop": DevelopConfig,
    "production": ProductionConfig,

    "default": Config,
}
