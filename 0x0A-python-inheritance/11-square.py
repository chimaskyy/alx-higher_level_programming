#!/usr/bin/python3
"""
This module contains class that inherits from
another class
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Iherits from the class Rectangle
    """

    def __init__(self, size):
        """Initialize an instance"""

        super().integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        return '[Square] {}/{}'.format(self.__size, self.__size)
