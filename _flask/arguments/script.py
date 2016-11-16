class Script(object):
    include = False
    py_import = ''

    def __init__(self, args):
        if args.flask_script is True:
            self.include = True
            self.py_import = '\nfrom flask_script import Manager, Shell'