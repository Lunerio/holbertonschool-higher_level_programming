#!/usr/bin/python3
"""module for a class declaration"""


class Student():
    """class student.
    with public attributes
    and method
    """
    first_name = None
    last_name = None
    age = None

    def __init__(self, first_name, last_name, age):
        """init method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return dict of instance"""
        new_dict = {}
        if attrs is None:
            return self.__dict__
        for i in attrs:
            if hasattr(self, i):
                new_dict[i] = getattr(self, i)
        return new_dict
