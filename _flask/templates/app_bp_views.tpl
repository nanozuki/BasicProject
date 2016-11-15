from flask import Flask, render_template
from flask_script import Manager

from . import main


@main.route('/')
def index():
    return render_template('index.html')
