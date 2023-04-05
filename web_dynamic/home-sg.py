#!/usr/bin/python3
""" Starts a Flash Web Application """
from models import storage
from models.food import Food
from models.place import Place
from models.tag import Tag
from models.place import Place
from os import environ
from flask import Flask, render_template, send_file
import uuid
import requests
app = Flask(__name__)
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/', strict_slashes=False)
# @app.route('/home', strict_slashes=False)
def sg():
    """ SG is alive! """

    foods = storage.all(Food).values()
    foods = sorted(foods, key=lambda k: k.review_date, reverse=True)

    places = storage.all(Place).values()
    places = sorted(places, key=lambda k: k.name)

    return render_template('home-sg.html',
                            foods=foods,
                            places=places)


@app.route('/food/name/<name>', strict_slashes=False)
def seach_food(name):
    """ searchs Foods """
    r = requests.get('http://172.26.250.210:5001/api/v1/food/name/' + name)
    
    places = storage.all(Place).values()
    places = sorted(places, key=lambda k: k.name)

    return render_template('home-sg.html',
                            foods=r.json(),
                            places=places)

@app.route('/place/name/<name>', strict_slashes=False)
def search_place(name):
    """ search Places """
    # search = storage(Place, 'name', name)

    r = requests.get('http://172.26.250.210:5001/api/v1/place/name/' + name)
    return render_template('location-sg.html',
                            places=r.json())
    
@app.route('/place', strict_slashes=False)
def list_place():
    """ lists all places """
    r = requests.get('http://172.26.250.210:5001/api/v1/place')
    return render_template('location-sg.html',
                             places=r.json())

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000, debug=True)
