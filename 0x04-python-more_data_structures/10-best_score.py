#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    num = 0
    for a, b in a_dictionary.items():
        if b > num:
            num = b
    for a, b in a_dictionary.items():
        if b == num:
            return a
