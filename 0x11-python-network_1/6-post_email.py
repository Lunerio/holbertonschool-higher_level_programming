#!/usr/bin/python3
"""Module that uses the POST method from requests package
"""


from sys import argv
import requests


if __name__ == '__main__':
    response = requests.post(argv[1], data={'email': argv[2]})
    print(response.text)
