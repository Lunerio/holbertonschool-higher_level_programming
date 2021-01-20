#!/usr/bin/python3
"""module for json function"""


def class_to_json(obj):
    """get a class and return dictionary"""
    lista = obj.__dict__
    return lista
