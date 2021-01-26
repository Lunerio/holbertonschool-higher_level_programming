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
            type(self).__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return json string object of argument"""
        if type(list_dictionaries) is not list and list_dictionaries is not None:
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
        lista = []
        name = str(cls.__name__) + ".json"
        if list_objs is None:
            with open(name, 'w') as f:
                f.write(cls.to_json_string(lista))
        else:
            for i in list_objs:
                lista.append(cls.to_dictionary(i))
            with open(name, 'w') as f:
                f.write(cls.to_json_string(lista))

    @staticmethod
    def from_json_string(json_string):
        """return json string representation as list"""
        if json_string is None or len(json_string) == 0:
            return []
        if type(json_string) is not str:
            raise TypeError("argument must be a string")
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creates an instance of the given class"""
        instance = cls(1, 1, 1, 1)
        cls.update(instance, **dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """return list of instances of class read from a file"""
        filename = str(cls.__name__) + ".json"
        lista_big = []
        lista_dicts = []
        text = ""
        try:
            with open(filename, 'r') as f:
                text = f.read()
            lista_dicts = cls.from_json_string(text)
            for i in lista_dicts:
                inst = cls.create(**i)
                lista_big.append(inst)
            return lista_big
        except IOError:
            return []
