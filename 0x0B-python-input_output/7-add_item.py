#!/usr/bin/python3
'''
This module contains a python script that adds all
argument to a python list and save them in a JSON
rep file
'''

import json
import sys


load_file = __import__('6-load_from_json_file').load_from_json_file
save_file = __import__('5-save_to_json_file').save_to_json_file


'''get command line args excluding the script name into a list'''
arguments = sys.argv[1:]

try:
    data = load_file("add_item.json")
except FileNotFoundError:
    data = []

data.extend(arguments)

save_file(data, "add_item.json")
