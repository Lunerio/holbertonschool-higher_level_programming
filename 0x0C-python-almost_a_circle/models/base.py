#!/usr/bin/python3
"""
module with the Base class
"""


import json



class Base():
    """base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return json string object of argument"""
        if type(list_dictionaries) is not list:
            raise TypeError("argument must be a list")
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """use json to write to a file a list of instances"""
        if type(list_objs) is not list:
            raise TypeError("argument must be a list")
        name = "{cls}.json"
        lista = []
        for i in list_objs:
            lista.append(i.__dict__)
        name = "Rectangle.json"
        with open(name, 'w') as f:
            json.dump(lista, f)
