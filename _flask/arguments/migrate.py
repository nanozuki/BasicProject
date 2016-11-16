class Migrate(object):
    include = False
    py_import = ''
    init = ''
    init_app = ''
    manage_import = ''
    manage_command = ''

    def __init__(self, args):
        if args.flask_migrate is True:
            self.include = True
            self.py_import = '\nfrom flask_migrate import Migrate'
            self.init = '\n\nmigrate = Migrate()\n'
            self.init_app = '\n    migrate.init_app(app, db)'
            self.manage_import = '\nfrom flask_migrate import MigrateCommand'
            self.manage_command = "\nmanager.add_command('db', MigrateCommand)"
