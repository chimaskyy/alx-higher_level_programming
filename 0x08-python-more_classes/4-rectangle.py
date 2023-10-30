#!/usr/bin/python3
"""
Define a Rectangle class
"""


class Rectangle:
    """Define a class rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError('width must be >= 0')
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

    def __str__(self):
        """string representation of intance"""
        rect = ""
        if self.__width != 0 or self.__height != 0:
            for i in range(self.__height):
                rect += "#" * self.__width
                if i < self.__height - 1:
                    rect += "\n"
        return rect

    def __repr__(self):
        """object representation of instance"""
        return "Rectangle({}, {})".format(self.__width, self.__height)
