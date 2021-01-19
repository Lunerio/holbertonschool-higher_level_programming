#!/usr/bin/python3
"""
This module has a function that reaturns
a boolean depending if an object is an
instance of a specified class
"""


def is_same_class(obj, a_class):
    """Return True if obj is an instance of
    a_class. Otherwise return False
    """
    return (type(obj) is a_class)
