#!/usr/bin/python3
''' script that starts a Flask web application '''

from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """ Function that close """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def cities():
    ''' Function that return list of all states '''
    amenities = storage.all(Amenity).values()
    states = storage.all(State).values()
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')