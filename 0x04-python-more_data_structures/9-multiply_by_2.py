#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = {}
    new.append({x: x * 2 for x in a_dictionary})
    return new
