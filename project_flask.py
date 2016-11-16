#!/usr/bin/env python
import argparse
import os
import shutil

from _flask import make_simple_project, make_project_with_blueprint
from _flask.arguments import Arguments
from _flask.requirements import render_requirements


def make_argparse():
    parser = argparse.ArgumentParser(description='Make Flask Projects')
    parser.add_argument('-b', dest='blueprint', action='store_true',
                        help='with blueprint(default name is main)')
    parser.add_argument('-n', dest='name', type=str, default='',
                        help='main script or blueprint(if have),'
                        'default "server.py" or "main"')
    parser.add_argument('-m', dest='models', action='store_true',
                        help='with models')
    parser.add_argument('-s', dest='flask_script', action='store_true',
                        help='with flask-script')
    parser.add_argument('--migrate', dest='flask_migrate', action='store_true',
                        help='with flask-migrate')
    parser.add_argument('target', metavar='target',
                        type=str, help='target dir')
    return parser


def make_project(args):
    current_path = os.getcwd()
    lib_path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(lib_path)
    shutil.rmtree('tmp', ignore_errors=True)
    if args.blueprint is False:
        make_simple_project(args)
    else:
        make_project_with_blueprint(args)
    render_requirements(args)
    os.chdir(current_path)
    shutil.move(os.path.join(lib_path, 'tmp'), args.target)


if __name__ == '__main__':
    parser = make_argparse()
    cmd_args = parser.parse_args()
    args = Arguments(cmd_args)
    make_project(args)
