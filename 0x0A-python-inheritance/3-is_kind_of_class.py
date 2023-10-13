#!/usr/bin/python3
'''
This modeule checks if obj is an instance of a class that
inherited from'
'''


def is_kind_of_class(obj, a_class):
    '''
    Function that checks for instances of object
    Return True or False if otherwise
    '''
    if isinstance(obj, a_class):
        return True
    return False
