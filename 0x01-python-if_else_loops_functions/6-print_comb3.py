#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if i < j:
            if i != 8 and j != 9:
                print('{}{}'.format(i, j), end=', ')
            elif i is 8 and j is 9:
                print('{}{}'.format(i,j))
