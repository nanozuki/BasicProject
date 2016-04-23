#!/usr/bin/env python3

import private_config
from app import create_app
from flask.ext.script import Manager, Shell
from flask.ext.migrate import MigrateCommand

app = create_app(private_config.CONFIG)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
