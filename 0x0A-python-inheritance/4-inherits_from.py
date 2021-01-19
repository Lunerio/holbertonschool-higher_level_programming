#!/usr/bin/python3
"""module for a function"""


def inherits_from(obj, a_class):
    """ true if subclass, false if not"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
