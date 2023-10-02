#!/usr/bin/python3
"""
This is a function that adds two integers
Returns sum of two integers
"""


def add_integer(a, b=98):
    """Takes two parameter
    Returns the sum of the two parameters
    """
    if type(a) is float:
        a = int(a)
    elif type(b) is float:
        b = int(b)
    elif type(a) not in (int, float):
        raise TypeError('a must be an integer')
    elif type(b) not in (int, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)
