import os
import private_config
import logging.handlers

base_dir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = private_config.SECRET_KEY
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # log
    LOG_PATH = os.path.join(base_dir, 'logs')

    @staticmethod
    def init_app(app):
        app.logger.setLevel(logging.DEBUG)
        debug_log = os.path.join(app.config["LOG_PATH"], 'debug.log')
        debug_log_handler = logging.handlers.RotatingFileHandler(
            debug_log, maxBytes=10000000, backupCount=100)
        debug_log_handler.setLevel(logging.DEBUG)
        debug_log_handler.setFormatter(logging.Formatter(
          '[%(asctime)s %(levelname)s in %(pathname)s %(lineno)d]:'
          ' %(message)s'))
        app.logger.addHandler(debug_log_handler)

        error_log = os.path.join(app.config["LOG_PATH"], 'error.log')
        error_log_handler = logging.handlers.RotatingFileHandler(
            error_log, maxBytes=10000000, backupCount=100)
        error_log_handler.setLevel(logging.ERROR)
        error_log_handler.setFormatter(logging.Formatter(
          '[%(asctime)s %(levelname)s in %(pathname)s %(lineno)d]:'
          ' %(message)s'))
        app.logger.addHandler(error_log_handler)


class DevelopConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = ''

    @staticmethod
    def init_app(app):
        Config.init_app(app)


class TestConfig(Config):
    DEBUG = True

    @staticmethod
    def init_app(app):
        Config.init_app(app)


class ProductionConfig(Config):
    DEBUG = False

    @staticmethod
    def init_app(app):
        app.logger.setLevel(logging.INFO)
        info_log = os.path.join(app.config["LOG_PATH"], 'info.log')
        info_log_handler = logging.handlers.RotatingFileHandler(
            info_log, maxBytes=10000000, backupCount=100)
        info_log_handler.setLevel(logging.DEBUG)
        info_log_handler.setFormatter(logging.Formatter(
          '[%(asctime)s %(levelname)s in %(pathname)s %(lineno)d]:'
          ' %(message)s'))
        app.logger.addHandler(info_log_handler)

        error_log = os.path.join(app.config["LOG_PATH"], 'error.log')
        error_log_handler = logging.handlers.RotatingFileHandler(
            error_log, maxBytes=10000000, backupCount=100)
        error_log_handler.setLevel(logging.ERROR)
        error_log_handler.setFormatter(logging.Formatter(
          '[%(asctime)s %(levelname)s in %(pathname)s %(lineno)d]:'
          ' %(message)s'))
        app.logger.addHandler(error_log_handler)


config = {
    "develop": DevelopConfig,
    "testing": TestConfig,
    "production": ProductionConfig,

    "default": Config,
}


app_config = config[private_config.CONFIG]
