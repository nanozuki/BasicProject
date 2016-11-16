from jinja2 import Environment, PackageLoader


_env = None


def render_file(template, target, **args):
    global _env
    if _env is None:
        _env = Environment(loader=PackageLoader('_flask', 'templates'))
    temp = _env.get_template(template)
    content = temp.render(**args)
    with open(target, 'w') as f:
        f.write(content)
