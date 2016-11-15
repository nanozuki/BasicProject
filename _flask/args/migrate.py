class Migrate(object):
    py_import = ''
    init = ''
    init_app = ''

    def __init__(self, args):
        if args.flask_migrate is True:
            self.py_import = '\nfrom flask_migrate import Migrate'
            self.init = '\n\nmigrate = Migrate()\n'
            self.init_app = '\n    migrate.init_app(app, db)'
