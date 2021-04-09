#!/usr/bin/python3
""" This module takes an URL and uses the POST request
    To set the email variable with a given argument
"""


from sys import argv
import urllib.request
import urllib.parse


if __name__ == '__main__':
    var = urllib.parse.urlencode({"email": argv[2]})
    var = var.encode('utf8')
    with urllib.request.urlopen(argv[1], var) as response:
        http_info = response.read()

    print(http_info.decode("utf-8"))
