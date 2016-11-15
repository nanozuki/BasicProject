from .migrate import Migrate
from .models import Models
from .script import Script


args = None


class Args(object):
    def __init__(self, cmd_args):
        self.blueprint = cmd_args.blueprint
        self.name = cmd_args.name
        if cmd_args.flask_migrate is True:
            cmd_args.models = True
            cmd_args.flask_script = True
        self.models = Models(cmd_args)
        self.flask_script = Script(cmd_args)
        self.flask_migrate = Migrate(cmd_args)
