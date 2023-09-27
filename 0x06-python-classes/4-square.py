#!/usr/bin/python3
"""class Square with size"""


class Square:

    """Empty Square class"""

    def __init__(self, size=0):

        """private size attribute initialized for Square instance"""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """This gets the size attribute/variable of the instance
        Helps to get the value of an attribute

        """
        return self.__size

    @size.setter
    def size(self, size):
        """This helps to change the value of an attribute
        Updates the size attribute
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Find area of current square"""
        return self.__size ** 2
