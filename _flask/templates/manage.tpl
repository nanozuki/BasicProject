#!/usr/bin/env python
import private_config
from app import create_app, db
from app.models import Example
from flask_script import Manager, Shell
from flask_migrate import MigrateCommand


app = create_app(private_config.CONFIG)
manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db, Example=Example)


manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
