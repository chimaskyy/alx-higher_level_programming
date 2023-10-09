#!/usr/bin/python3
'''
This module contains a single function
It prints the list of available method and attribute of an object
'''


def lookup(obj):
    '''Function that prints list of available attribute and
    methods of an object
    Arg:
        obj: The object to check
    Return: List of methods and attributes of obj
    '''
    return dir(obj)
