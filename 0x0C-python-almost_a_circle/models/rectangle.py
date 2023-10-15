#!/usr/bin/python3
'''
This module contains a class Rectangle
It inherits from the `Base` class
'''

from models.base import Base


class Rectangle(Base):
    '''
    class Rectangle inheriting from Base class
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        Rectangle objects initialised
        Args:
            width: width of the rectangle
            height: height of the rectangle
            x: x-coordinate
            y: y-coordinate
            id: ID of the rectangle
        '''
        if type(width) is not int:
            raise TypeError('width must be an integer')
        elif width <= 0:
            raise ValueError('width must be > 0')
        elif type(height) is not int:
            raise TypeError('height must be an integer')
        elif height <= 0:
            raise ValueError('height must be > 0')
        elif type(x) is not int:
            raise TypeError('x must be an integer')
        elif x < 0:
            raise ValueError('x must be >= 0')
        elif type(y) is not int:
            raise TypeError('y must be an integer')
        elif y < 0:
            raise ValueError('y must be >= 0')

        # call Base class constructor
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @staticmethod
    def validate_value(**kwargs):
        """
        This is used to validate Rectangle attributes
        args:
            **kwargs: variable number of keyword argument

        for key, value in kwargs.items():
            if key == "width" or key == "height":
                if type(value) is not int:
                    raise TypeError('{} must be an integer'.format(key))
                if value <= 0:
                    raise ValueError('{} must be > 0'.format(key))
            elif key == "x" or key == "y":
                if type(value) is not int:
                    raise TypeError('{} must be an integer'.format(key))
                if value <= 0:
                    raise ValueError('{} must be >= 0'.format(key))"""

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value <= 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value <= 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        '''calculates the area of a rectangle'''
        return self.__width * self.__height

    def display(self):
        '''print rect instances with char #'''
        print("\n" * self.y, end="")
        for num in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width, end="")
            print()

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".\
            format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        '''
        Update attri of Rectangle instance
        Args:
            *args: Variable number of positional argument(id,width,heigh,x,y)
            kwargs: Variable number of Keyword args'''
        if args != ():
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        '''Return dict representation of rectangle'''
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
            }
