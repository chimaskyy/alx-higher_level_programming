#!/usr/bin/python3
'''
This module containa a class and 2 method
integer_validator: Validates integer values
area: does nothing
'''


class BaseGeometry:
    '''
    class defined
    '''

    def area(self):
        '''a public instance'''
        raise Exception('area() is not implemented')
    
    def integer_validator(self, name, value):
        '''Validates values passed as integer
        or not
        '''
        if type(value) is not int:
            raise TypeError('{} must be a integer'.format(name))
        if value <= 0:
             raise ValueError('{} must be greater than 0'.format(name))

class Rectangle(BaseGeometry):
    """
    subclass of the base class BaseGeometry
    """
    def __init__(self, width, height):
        """
        initialize instances
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)

        self.__width = width
        self.__height = height