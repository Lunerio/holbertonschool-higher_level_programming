#!/usr/bin/python3
"""more json things"""


import json


def load_from_json_file(filename):
    """read from a file and decode"""
    with open(filename) as f:
        obj = json.load(f)
    return obj
