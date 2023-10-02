#!/usr/bin/python3
"""
This module creates and defines class Rectangle
"""


class Rectangle:
    """Defined class rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        
    @property
    def width(self):
         """Gets width"""
         return self.__width

    @width.setter
    def width(self, width):
        """width setter"""
        if type(width) is not int:
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError('width must be >= 0')
        self.__width = width

    @property
    def height(self):
        """gets height"""
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height

