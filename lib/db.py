#!/usr/bin/env/python

# ---------------------------------------------------------------------
#     This file is meant to be an example format for a database plugin.
#  depending on the back-end that you use, you can fill in the body of
#  the listed subroutines. It's upto you to decide how frequently you
#  want to connect to your database, crash protection and so on :)
# ---------------------------------------------------------------------

import datetime;

# ---------------------------------------------------------------------
# ELEMENT - this is the basic unit for all journal entries
# ---------------------------------------------------------------------

class Element:

    date            #-- some form of date representation
    tags            #-- a list of string tags for this entry
    threadid        #-- unique thread-id for tracking tasks, 0 if not assigned
    text            #-- text of the entry
    verbose         #-- additional text for the element


# ---------------------------------------------------------------------
# THREAD - unit for tracking threads
# ---------------------------------------------------------------------

class Thread:

    name            #-- full heading of the task
    nick            #-- a tagname used for matching an element to a thread
    date            #-- date the task was created
    description     #-- brief description of task
 
    
# ---------------------------------------------------------------------
# Global vars ?
#journal = []
#threads = []


# ---------------------------------------------------------------------
# Interfaces: hook up your db to answer the following
# ---------------------------------------------------------------------

def add(el):
""" Adds a new element to the journal """

def insert(day, el):
""" Inserts element on a particular day """


def getbydate(start, end):
""" Gets a list of elements between two dates """

def getbythread(tid):
""" Gets a list of elements in a thread"""

def addthread(thread):
""" Inserts a thread to the db"""

def getthread(tid):
""" Returns the thread corresponding id : tid"""


