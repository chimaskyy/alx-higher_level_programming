#!/usr/bin/python3
"""class Square with size"""


class Square:

    """Empty Square class"""
    def __init__(self, size=0, position=(0, 0)):

        """private size attribute initialized for Square instance/object"""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        pos = position
        if len(pos) != 2 or type(pos[0]) is not int or \
                type(pos[1]) is not int or pos[0] < 0 or pos[1] < 0:
            raise TypeError("position must be a tupple of 2 positive integers")
        else:
            self.__position = position

    @property
    def size(self):
        """This gets the size attribute/variable of the instance
        Helps to get the value of an attribute"""
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
    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, value):
        if len(value) != 2 or type(value[0]) is not int or \
                type(value[1]) is not int or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tupple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Find area of current square"""
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
            return
        print("\n" * self.__position[1], end="")
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size, end="")
            print()