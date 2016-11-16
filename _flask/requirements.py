require = [
    'Flask',
    'ipython',
    'flake8'
]


def render_requirements(args):
    if args.models.include is True:
        require.append('Flask-SQLAlchemy')
    if args.script.include is True:
        require.append('Flask-Script')
    if args.migrate.include is True:
        require.append('Flask-Migrate')
    with open('tmp/requirements.txt', 'w') as f:
        f.write('\n'.join(require))
