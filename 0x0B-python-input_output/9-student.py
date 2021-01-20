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

    def to_json(self):
        """return dict of instance"""
        return self.__dict__
