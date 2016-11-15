class Models(object):
    py_import = ''

    def __init__(self, args):
        if args.models is True:
            self.py_import = 'from .models import db'
            self.init_app = '\n    db.init_app(app)'
