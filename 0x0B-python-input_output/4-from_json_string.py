#!/usr/bin/python3
'''
This module contains a single function
'''
import json


def from_json_string(my_str):
    '''
    Function that returns JSON rep of an object
    '''
    return json.loads(my_str)
