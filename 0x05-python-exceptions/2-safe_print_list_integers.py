#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        try:
            for i in range(x):
                print("{:d}".format(my_list[i]), end="")
            print()
        except(IndexError):
            print()