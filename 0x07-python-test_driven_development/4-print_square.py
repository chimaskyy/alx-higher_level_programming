#!/usr/bin/python3
"""
This module print a square with the character #
Size must be a positive integer
"""


def print_square(size):
    """Function that prints a square with the character #
    Arg:
        size: Size of the square
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    elif type(size) is float and size < 0:
        raise TypeError('size must be an integer')
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
