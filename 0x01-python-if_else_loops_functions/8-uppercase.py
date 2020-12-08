#!/usr/bin/python3
def uppercase(str):
    for s in range(len(str)):
        c = ord(str[s])
        if c > 96 and c < 123:
            c = c - 32
        print('{:c}'.format(c), end='')
    print()
