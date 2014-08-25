#!/usr/bin/env python

# Just for accessing the app standalone
#

import pickle
import sys


sys.path.append('lib/')
from bottle import route
from bottle import view
from bottle import run
from bottle import static_file


@route('/html/<filename>')
def server_static(filename):
    return static_file(filename, root='./html/')

@route('/<user>/app')
@route('/app')
@view('html/index')
def app(user = 'bricam01'):
    return dict(user=user)

run(host='localhost', port=8080, debug=True)
