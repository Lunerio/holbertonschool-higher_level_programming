#!/usr/bin/python3
"""this module contains a function that checks
if an object is an instance of a subclass that inherited
from a given class
"""


def inherits_from(obj, a_class):
    """return true if subclass, false if not"""
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
