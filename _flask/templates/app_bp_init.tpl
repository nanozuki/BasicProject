from flask import Blueprint

{{ name }} = Blueprint('{{ name }}', __name__)

from . import views
