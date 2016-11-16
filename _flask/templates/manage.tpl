#!/usr/bin/env python
import private_config
from app import create_app{{ models.manage_import }}{{ script.py_import }}{{ migrate.manage_import }}


app = create_app(private_config.CONFIG)
manager = Manager(app)


def make_shell_context():
    return dict(app=app{{ models.manage_context }})


manager.add_command('shell', Shell(make_context=make_shell_context)){{ migrate.manage_command }}


if __name__ == '__main__':
    manager.run()
