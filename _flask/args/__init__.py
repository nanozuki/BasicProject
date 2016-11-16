from .migrate import Migrate
from .models import Models
from .script import Script


args = None


class Args(object):
    def __init__(self, cmd_args):
        if cmd_args.flask_migrate is True:
            cmd_args.models = True
            cmd_args.flask_script = True
        if cmd_args.blueprint is True:
            cmd_args.flask_script = True
        self.blueprint = cmd_args.blueprint
        self.name = cmd_args.name
        self.models = Models(cmd_args)
        self.flask_script = Script(cmd_args)
        self.flask_migrate = Migrate(cmd_args)
