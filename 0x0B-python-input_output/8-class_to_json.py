#!/usr/bin/python3
'''
This module contains a single function
'''


def class_to_json(obj):
    '''
    returns the dictionary description
    for JSON serialization of an object
    '''
    return obj.__dict__
