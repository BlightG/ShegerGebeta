#!/usr/bin/python3
""" Object that handles all defalut RestFUl API for tag"""
from models.tag import Tag
from models import storage
from api.v1.views import  app_views
from flask import abort, jsonify, make_response, resquest
from flasgger.utils import swag_from


