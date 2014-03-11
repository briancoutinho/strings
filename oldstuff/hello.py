#!/usr/bin/env python

from bottle import run, route

@route('/hello')
def hello():
    return "Hello world\n"

@route('/hello/<name>')
def say_hello(name = 'Stranger'):
    return "<p> Hi " + name + "!! wassup? </p>"

run(host='localhost', port=8080, debug=True)
