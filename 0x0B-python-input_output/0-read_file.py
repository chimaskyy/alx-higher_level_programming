#!/usr/bin/python3
'''
The module contains a single function
'''


def read_file(filename=""):
    '''
    Function that reads a text file and
    prints its output to stdout
    '''
    with open(filename, 'r', encoding="utf-8") as f:
        data = f.read()
        print(data)
