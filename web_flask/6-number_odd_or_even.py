#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """returns Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """returns C, followed by the value of the text"""
    return "C " + text.replace("_", " ")


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """returns "Python", followed by the value of the text"""
    return "Python " + text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """returns "n is a number" only if n is an integer"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """returns "n is a number" only if n is an integer"""
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """returns "Number: n is even|odd" only if n is an integer"""
    if (n % 2) == 0:
        even_odd = "is even"
        return render_template('6-number_odd_or_even.html', number=n,
                               even_odd=even_odd)
    else:
        even_odd = "is odd"
        return render_template('6-number_odd_or_even.html',
                               number=n, even_odd=even_odd)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')