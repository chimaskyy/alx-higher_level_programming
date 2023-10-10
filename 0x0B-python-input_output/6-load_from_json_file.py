#!/usr/bin/python3
'''
This module contains a single function
'''
import json


def load_from_json_file(filename):
    '''
    Function that writes an Object to a text file
    using a JSON representation
    '''
    with open(filename, 'r') as f:
        return json.load(f)
