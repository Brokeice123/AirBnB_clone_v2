#!/usr/bin/python3
"""
Script that starts a Flask web application.
It listens on 0.0.0.0, port 5000.
Has routes:
    - / : displays "Hello HBNB!"
    - /hbnb : displays "HBNB"
    - /c/<text> : display "C" followed by the value of the text
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Returns C followed by the value of the text"""
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
