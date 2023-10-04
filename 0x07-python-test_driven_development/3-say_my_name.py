#!/usr/bin/python3
"""
This module contains a function that prints first and last name
Inputs must be strings
"""


def say_my_name(first_name, last_name=""):
    """
    Function that prints first and last name
    Args:
        first_name: User first name
        last_name: User lat name
    """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    elif type(last_name) is not str:
        raise TypeError('first_name must be a string')
    if len(first_name) == 0:
        print(last_name)
    print("My name is {} {}".format(first_name, last_name))
