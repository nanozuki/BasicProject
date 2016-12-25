from config import config
from flask import Flask{{migrate.py_import}}{{models.py_import}}
{{models.init}}
{{migrate.init}}

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
{{models.init_app}}{{migrate.init_app}}

    from .{{name}} import {{name}}
    app.register_blueprint({{name}}, url_prefix='/')

    return app
