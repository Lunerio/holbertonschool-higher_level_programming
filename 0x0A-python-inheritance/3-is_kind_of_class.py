#!/usr/bin/python3
"""
This module contains a function that checks
if an object is an instance of a class or a
subclass
"""


def is_kind_of_class(obj, a_class):
    """return true if instance, false if not"""
    return (isinstance(obj, a_class))
