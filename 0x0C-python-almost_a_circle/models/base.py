#!/usr/bin/python3
"""
module with a base class
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

    def to_json_string(list_dictionaries):
        """return json string object of argument"""
        if type(list_dictionaries) is not list:
            raise TypeError("argument must be a list")
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
