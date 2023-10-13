#!/usr/bin/python3
'''
This module checks if an object is an instance of a clas
'''


def is_same_class(obj, a_class):
    """
    Function that checks if an object is an instance of a class
    Returns True or False if otherwise
    """
    if type(obj) is a_class:
        return True
    return False
