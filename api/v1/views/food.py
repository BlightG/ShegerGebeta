#!/usr/bin/python3
""" Object that handles all defalut RestFUl API for food"""
from models.food import Food
from models import storage
from datetime import datetime
from api.v1.views import  app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/food/name/<string>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/food/food_name.yml')
def food_name(string):
    """ Retrieves food having a specifed name """
    foods = storage.search(Food, 'food_name', string)
    food_list = []
    for food in foods:
        food_list.append({food.id: food.food_name})
    return jsonify(food_list)


@app_views.route('/food/price/<price>', methods=['GET'], strict_slashes=False)
@swag_from('documnetation/food/food_price.yml')
def food_price(price):
    """ Retrives food of a specifed Price """
    if isinstance(price, float) is None:
        return abort(404)

    prices = storage.search(Food, 'price', price)
    price_list = []
    for price in prices:
        price_list.append({price.id: price.price})
    return jsonify(price_list)


@app_views.route('/food/date/<date_time>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/food/food_date.yml')
def food_date(date_time):
    """ Retrives food of a specified review date """
    # if isinstance(date_time, datetime):
    #     return abort(404)

    dates = storage.search(Food, 'review_date', date_time)
    date_list = []
    if dates:
        for date in dates:
            date_list.append({date.id: date.review_date})
    return jsonify(date_list)
