#!/usr/bin/python3
"""Defined class Square with size"""


class Square:
    """Empty Square class"""
    def __init__(self, size=0):
        """private size attribute initialized for Square instance"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
