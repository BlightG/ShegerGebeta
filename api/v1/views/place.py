#!/usr/bin/python3
""" Object that handles all defalut RestFUl API for place"""
from models.place import Place
from models.food import Food
from models import storage
from api.v1.views import  app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from

@app_views.route('/place', methods=['GET'], strict_slashes=False)
@swag_from('documentation/place/place.yml')
def get_place():
    """ retrives all foods for a place """
    places = storage.all(Place)
    print(places)
    if len(places) == 0:
        return jsonify({})
    place_list = []
    for place in places.values():
        place_list.append(place.to_dict())
    return jsonify(place_list)

@app_views.route('/place/<name>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/place/place_menu.yml')
def get_menu(name):
    """ retrives all foods for a place """
    places = storage.search(Place, 'name', name)
    
    if len(places) == 0:
        return jsonify({})

    place_id = places[0].id
    all_food = storage.search(Food, 'place_id', place_id)
    list_food = []
    
    for food in all_food:
        list_food.append(food.to_dict())
    return jsonify(list_food)

@app_views.route('/place/name/<name>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/place/place_name.yml')
def get_name(name):
    """ retrives a place serached by its name """
    results = storage.search(Place, 'name', name)
    result_list = []
    for result in results:
        result_list.append(result.to_dict())
    return jsonify(result_list)