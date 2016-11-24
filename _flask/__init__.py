import os
import shutil

from .render import render_file


def make_simple_project(args):
    pass


def make_project_with_blueprint(args):
    shutil.copytree('_flask/basic/blueprint', 'tmp')
    make_app(args)


def make_app(args):
    os.mkdir('tmp/app')
    render_file('app_init.tpl', 'tmp/app/__init__.py',
                models=args.models, migrate=args.migrate, name=args.name)
    if args.models.include is True:
        render_file('models.tpl', 'tmp/app/models.py')
    make_blueprint(args)
    render_file('manage.tpl', 'tmp/manage.py', script=args.script,
                migrate=args.migrate, models=args.models)


def make_blueprint(args):
    os.mkdir('tmp/app/{0}'.format(args.name))
    render_file('app_bp_init.tpl', 'tmp/app/{0}/__init__.py'.format(args.name),
                name=args.name)
    render_file('app_bp_views.tpl', 'tmp/app/{0}/views.py'.format(args.name),
                name=args.name)
