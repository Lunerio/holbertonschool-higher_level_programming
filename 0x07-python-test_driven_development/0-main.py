#!/usr/bin/python3
import math
add_integer = __import__('0-add_integer').add_integer

print(add_integer(12, 12e500000))
print(add_integer(1a, 2))
print(add_integer(10, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)
