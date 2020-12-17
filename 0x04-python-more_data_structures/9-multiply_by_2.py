#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = {x: b * 2 for x, b in a_dictionary.items()}
    return new
