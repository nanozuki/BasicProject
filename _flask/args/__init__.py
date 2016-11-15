class Args(object):
    def __init__(args):
        self.blueprint = blueprint_args(args)
        self.name = name_args(args)
        self.models = models_args(args)
        self.flask_script = script_args(args)
        self.flask_migrate = migrate_args(args)
