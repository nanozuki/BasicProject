from flask import Flask, render_template{{script.py_import}}

from . import main


@main.route('/')
def index():
    return render_template('index.html')
