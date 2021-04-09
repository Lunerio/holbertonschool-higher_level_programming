#!/usr/bin/python3
""" This module uses requests to get information from a user
    from GITHUB API
"""


from sys import argv
import requests


if __name__ == '__main__':
    response = requests.get('https://api.github.com/user',
                            auth=(argv[1], argv[2]))
    dict = response.json()
    print('{}'.format(dict.get('id')))
