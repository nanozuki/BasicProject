class Models(object):
    include = False
    py_import = ''
    init_app = ''
    manage_import = ''
    manage_context = ''

    def __init__(self, args):
        if args.models is True:
            self.include = True
            self.py_import = '\nfrom flask_sqlalchemy import SQLAlchemy'
            self.init = '\n\ndb = SQLAlchemy()'
            self.init_app = '\n    db.init_app(app)'
            self.manage_import = ', db\nfrom app.models import Example'
            self.manage_context = ', db=db, Example=Example'
