#!/usr/bin/python3
"""Use the requests module to print status error number
"""


from sys import argv
import requests


if __name__ == '__main__':
    response = requests.get(argv[1])
    if response.status_code >= 400:
        print('Error code: {}'.format(response.status_code))
    else:
        print(response.text)
