#!/usr/bin/python3
"""
This module has a method that returns
a list with the dictionary of an object
"""


def lookup(obj):
    """
    return a list with the dict of obj
    """

    return (list(obj.__class__.__dict__))