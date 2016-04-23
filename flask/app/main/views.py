from flask import Flask, render_template
from flask.ext.script import Manager

from . import main


@main.route('/')
def index():
    return render_template('index.html')
