#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        res = None
        return None
    finally:
        print("Inside result: {}".format(res))
