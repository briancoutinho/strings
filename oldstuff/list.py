#!/usr/bin/env python

from bottle import run, route, get, post, request
import pickle

def save_list(list_dict):
   pickle.dump( list_dict, open("list.pickle", 'wb') )


def load_list():
    return  pickle.load( open("list.pickle", 'rb') )

def build_page(lst):
    form = """
    <form action="list" method="post">
         Item=
         index : <input name=index type="text"/> 
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

    for i in sorted(lst.keys(), key=int):
        text += '<p>[' + str(i) + '] : ' + lst[i] + '</p>\n'
    text += form
    return text

@get('/list')
def dump_all():
    return build_page(load_list())

@post('/list')
def add_item():
    lst = load_list()

    index = request.forms.get('index')
    value = request.forms.get('value')

    lst[index] = value
    save_list(lst)

    return build_page(lst)

@route('/reset')
def reset():
    list_dict = {'1': 'Wakeup', '2': 'Brush teeth', '3' : 'Bath (verb)'}
    save_list(list_dict)

run(host='localhost', port=8080, debug=True)
