from flask import Blueprint

main = Blueprint({{ name }}, __name__)

from . import views
