class Script(object):
    py_import = ''

    def __init__(self, args):
        if args.flask_script is True:
            self.py_import = '\nfrom flask_script import Manager'