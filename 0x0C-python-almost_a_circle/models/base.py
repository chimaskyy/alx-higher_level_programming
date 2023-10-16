#!/usr/bin/python3
'''This module contains a class'''

import json



class Base:
    '''This is the base class
    '''

    '''private class attribute'''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON serialization of a dicts list.
        Args:
            list_dictionaries: list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            list_dictionaries = "[]"
        return json.dumps(list_dictionaries)
    
    @staticmethod
    def from_json_string(json_string):
        '''parse json string and return list of dict
        Args:
            json_string: json string representing dict list
        Return: Returns list of dictionary fo json string
        '''    
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)
    
    @classmethod
    def save_to_file(cls, list_objs):
        '''save json string to a file'''
        if list_objs is None or list_objs == []:
            to_list_dict = []
        else:
            to_list_dict = [obj.to_dictionary() for obj in list_objs]
        f = cls.__name__ + ".json" # generate file for json
        with open(f, "w", encoding="utf-8") as jfile:
            '''write json str rep of list to the file'''
            jfile.write(Base.to_json_string(to_list_dict))

    @classmethod
    def create(cls, **dictionary):
        """creates a class from a dict of arguments"""
        
        from models.rectangle import Rectangle
        from models.square import Square
        if cls.__name__ == 'Rectangle':
            dummy = Rectangle(1, 1)
        elif cls.__name__ == 'Square':
            dummy = Square(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Loads data from file and uses it to get instances associated
        Returns:
            a list of instances:
        """
        filename = "{}.json".format(cls.__name__)

        try:
            with open(filename, encoding="utf-8") as f:
                string = f.read()
        except FileNotFoundError:
            return []

        json = cls.from_json_string(string)
        instances = [cls.create(**element) for element in json]
        return instances




    