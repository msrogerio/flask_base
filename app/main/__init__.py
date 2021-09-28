from flask import Blueprint

_main = Blueprint('_main', __name__)

from . import controllers