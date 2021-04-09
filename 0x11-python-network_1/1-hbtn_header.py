#!/usr/bin/python3
""" Request an URL from argument and display the value of
    X-Request-Id from the header
"""


from sys import argv
import urllib.request


if __name__ == '__main__':
    with urllib.request.urlopen(argv[1]) as response:
        http = response.getheader('X-Request-Id')

    print(http)
