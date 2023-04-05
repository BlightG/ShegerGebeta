#!/usr/bin/python3
""" Bluebrint for API """

from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.place import *
from api.v1.views.food import *