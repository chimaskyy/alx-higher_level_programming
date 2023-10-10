#!/usr/bin/python3
'''
This module contains a single function
'''


def write_file(filename="", text=""):
    '''
    Function that writes to a text file
    '''
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
