#!/usr/bin/python3
'''
This module contains a defined class
'''


class Student:
    '''defined class'''

    def __init__(self, first_name, last_name, age):
        '''initialize instance/variable attributes'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''
        retrieves a dictionary representation of a Student
        '''
        if attrs is None:
            return self.__dict__
        else:
            attributes = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    attributes[key] = value
            return attributes
    
    def reload_from_json(self, json):
        '''replaces all attributes of the Student instance'''
        if isinstance(json, dict):
            for key, value in json.items():
                setattr(self, key, value)
