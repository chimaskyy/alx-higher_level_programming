#!/usr/bin/python3
'''
This module contains a single function
'''
import json


def load_from_json_file(filename):
    '''
    Function that loads an object from a JSON file and returns it
    filename (str): The name of the JSON file to read.
    Returns python file loaded to JASOn file
    '''
    with open(filename, 'r') as f:
        return json.load(f)
