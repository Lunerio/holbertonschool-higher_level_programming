#!/usr/bin/python3
""" This module takes an URL and uses the POST request
    To set the email variable with a given argument
"""


from sys import argv
import urllib.request
import urllib.error


if __name__ == '__main__':
    try:
        with urllib.request.urlopen(argv[1]) as response:
            http_info = response.read()
        print(http_info.decode("utf-8"))
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
