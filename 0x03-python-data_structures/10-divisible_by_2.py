#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new = []
    for i in my_list:
        if i % 2 == 0:
            new.append(True)
        elif i % 2 != 0:
            new.append(False)
    return new
