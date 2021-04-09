#!/usr/bin/python3
""" This module uses the urllib package to fetch an url
"""


import urllib.request


if __name__ == '__main__':
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        http = response.read()
        body = http.decode()

    print('Body response:')
    print('\t- type: {}'.format(type(http)))
    print('\t- content: {}'.format(http))
    print('\t- utf8 content: {}'.format(body))
