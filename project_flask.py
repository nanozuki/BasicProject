#!/usr/bin/env python3
import argparse

from _flask.args import Args, args
from _flask import make_simple_project, make_project_with_blueprint


def make_argparse():
    parser = argparse.ArgumentParser(description='Make Flask Projects')
    parser.add_argument('-b', dest='blueprint', action='store_true',
                        help='with blueprint(default name is main)')
    parser.add_argument('-n', dest='name', type=str, default='',
                        help='main script or blurprint(if have),'
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


def make_project():
    if args.blueprint is False:
        make_simple_project()
    else:
        make_project_with_blueprint()


if __name__ == '__main__':
    parser = make_argparse()
    cmd_args = parser.parse_args()
    args = Args(cmd_args)
    make_project()
