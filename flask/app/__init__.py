from flask import Flask

from flask.ext.migrate import Migrate

from .main import main
from .models import db
from config import config


migrate = Migrate()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(main, url_prefix='/')

    return app
