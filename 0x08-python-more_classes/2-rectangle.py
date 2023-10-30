#!/usr/bin/python3
"""
This module defines a class Rectangle
Returns the rectangle area and its perimeter
"""


class Rectangle:
    """define rectangle"""
    def __init__(self, width=0, height=0):
        """instanciate two attribute"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, width):
        """width setter"""
        if type(width) is not int:
            raise TypeError('width must be an integer')
        elif width < 0:
            raise valueError('width must be >= 0')
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        peri = 2 * (self.__width + self.__height)
        if self.__width == 0 or self.__height == 0:
            peri = 0
        return peri
