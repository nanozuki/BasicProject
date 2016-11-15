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
