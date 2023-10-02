#!/usr/bin/python3
"""
Define a rectangle class
"""


class Rectangle:
    """Define class"""

    """public class attribute"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
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

    def __str__(self):
        rect = ""
        if self.__width != 0 and self.__height != 0:
            for i in range(self.__height):
                rect += str(self.print_symbol) * self.__width
                if i < self.__height - 1:
                    rect += "\n"
        return rect

    def __repr__(self):
        """object representation of instance"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")

        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if type(rect_2) is not Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
    @classmethod
    def square(cls, size=0):
        new = cls(size, size)
        return new