#!/usr/bin/env python

# Basic version - 0.0.01
#

import pickle
import sys


from bottle import run, route, get, post, request
sys.path.append('../lib')

def save_list(index_list):
   pickle.dump( index_list, open("list.pickle", 'wb') )


def load_list():
    return  pickle.load( open("list.pickle", 'rb') )

def build_page(lst):
    form = """
    <form action="list" method="post">
         Item=
         tag : <input name=tag type="text"/> 
         text  : <input name=value  type="text"/> 
         <input value"Add" type="submit"/>
    </form>
    """
    text = '''
    <html>
    <head>
    <title> List page </title>
    </head>
    <body>
    '''

    for i in lst:
        text += '<p>[' + str(i['tag']) + '] : ' + i['value'] + '</p>\n'
    text += form
    return text

@get('/list')
def dump_all():
    return build_page(load_list())

@post('/list')
def add_item():
    lst = load_list()

    tag = request.forms.get('tag')
    value = request.forms.get('value')

    lst.append(dict({'tag' : tag , 'value' : value }))
    save_list(lst)

    return build_page(lst)

@route('/reset')
def reset():
    index_list = []
    index_list.append({'tag': 'mack', 'value' : 'boot'})
    save_list(index_list)

reset()
run(host='localhost', port=8080, debug=True)
