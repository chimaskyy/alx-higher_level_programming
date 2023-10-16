#!/usr/bin/python3
"""
This module contains the class Square
It inherits from the class Rectangle
"""

from models.rectangle import Rectangle

class Square(Rectangle):
    '''class Square inherits from Rectangle class'''
    
    def __init__(self, size, x=0, y=0, id=None):
        """Instantiate a square
        Args:
            size: size of the square
            x: x coordinate
            y: y coordinate
            id: identity of the square
            """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".\
            format(self.id, self.x, self.y, self.width)
    
    @property
    def size(self):
        """getter for size"""
        return self.width
    
    @size.setter
    def size(self, size):
        '''setter for size'''
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        '''
        Update attri of Rectangle instance
        Args:
            *args: Variable number of positional argument(id,width,heigh,x,y)
            kwargs: Variable number of Keyword args
        '''
        if args != ():
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        '''Return dict representation of rectangle'''
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
            }
    