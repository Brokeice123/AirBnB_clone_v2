#!/usr/bin/python3
"""
Script that starts a web flask
Listens on 0.0.0.0, port 5000
Uses storage to fetch data
Route:
    /states_list: list all states
"""

from flask import Flask, render_template
from models.state import State
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """List all states"""
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
