#!/usr/bin/python3
'''This module contains a class'''


class Base:
    '''This is the base class
    '''

    '''private class attribute'''
    __nb_objects = 0
    
    #class constructor
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
            
