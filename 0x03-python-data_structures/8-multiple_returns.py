#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    char = ""
    if length == 0:
        char = None
    else:
        char = sentence[0]
    new_t = (length, char)
    return new_t
