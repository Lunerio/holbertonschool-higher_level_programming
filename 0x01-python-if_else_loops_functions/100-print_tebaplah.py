#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 is 1:
        c = (i - 32)
    else:
        c = i
    print('{:c}'.format(c), end='')
