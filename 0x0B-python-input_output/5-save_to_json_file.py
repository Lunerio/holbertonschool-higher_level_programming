#!/usr/bin/python3
"""module with json function"""


import json


def save_to_json_file(my_obj, filename):
    """open file and write string rep with json"""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
