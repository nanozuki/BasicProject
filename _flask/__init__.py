import os

from .render import render_file


args = None


def make_simple_project():
    pass


def make_project_with_blueprint():
    os.mkdir(args.target)
    os.mkdir('tmp')
    make_app()


def make_app():
    os.mkdir('tmp/app')
    render_file('app_init.tpl', 'tmp/app/__init__.py',
                models=args.models, migrate=args.migrate)
    if args.models is True:
        render_file('models.tpl', 'tmp/app/models.py')
    make_blueprint()
    render_file('manage.tpl', )


def make_blueprint():
    os.mkdir('tmp/app/{0}'.format(args.name))
    render_file('app_bp_init.tpl', 'tmp/app/{0}/__init__.py'.format(args.name),
                name=args.name)
    render_file('app_bp_views.tpl', 'tmp/app/{0}/views.py'.format(args.name),
                script=args.flask_script)
