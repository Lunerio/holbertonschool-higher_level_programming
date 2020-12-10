#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    sum = 0
    for i in range(1, len(argv)):
        x = int(argv[i], 10)
        sum = sum + x
    print("{:d}".format(sum))
