from flask import Flask, render_template

from . import {{ name }}


@{{ name }}.route('/')
def index():
    return render_template('index.html')
