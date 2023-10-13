#!/usr/bin/python3
'''
This module contains a class that inherits from `int`
'''


class MyInt(int):
    '''defined class
    inherits from int base class
    '''

    def __eq__(self, i):
        '''equal to comparison magic method
        overide == operator and inverts it's behavior
        '''
        return not super().__eq__(i)

    def __ne__(self, i):
        '''not equal to comparison magic method
        overide != operator and inverts it's behavior
        '''
        return super().__eq__(i)
