from .migrate import Migrate
from .models import Models
from .script import Script


args = None


class Arguments(object):
    def __init__(self, cmd_args):
        self.target = cmd_args.target
        if cmd_args.name == '':
            if cmd_args.blueprint is True:
                cmd_args.name = 'main'
            else:
                cmd_args.name = 'server.py'
        if cmd_args.flask_migrate is True:
            cmd_args.models = True
            cmd_args.flask_script = True
        if cmd_args.blueprint is True:
            cmd_args.flask_script = True
        self.blueprint = cmd_args.blueprint
        self.name = cmd_args.name
        self.models = Models(cmd_args)
        self.script = Script(cmd_args)
        self.migrate = Migrate(cmd_args)
