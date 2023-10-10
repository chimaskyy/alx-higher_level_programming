#!/usr/bin/python3
'''
This module contains a single function
'''
import json


def to_json_string(my_obj):
    '''
    Function that returns JSON rep of an object
    '''
    return json.dumps(my_obj)
