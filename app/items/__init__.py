from flask import Blueprint

items_blueprint = Blueprint('items', __name__)

from . import views