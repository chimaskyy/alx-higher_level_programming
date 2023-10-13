#!/usr/bin/python3
'''
This module contains a single function
'''


def add_attribute(self, attribute, value):
    '''
    Adds new attribute if possible
    '''
    if hasattr(self, '__dict__'):
        setattr(self, attribute, value)
    else:
        raise TypeError("can't add new attribute")
