#!/usr/bin/python3
'''
This module checks if an obj is an instance of a
class inherited(directly or indirectly) from the class
'''


def inherits_from(obj, a_class):
    '''
    Function that checks obj instance
    Returns True or False if otherwise
    '''
    return issubclass(type(obj), a_class) and type(obj) is not a_class
