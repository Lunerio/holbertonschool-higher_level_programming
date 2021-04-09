#!/usr/bin/python3
""" This module uses requests package to request a POST method
    and set parameters. Also checks if the response is Json
"""


from sys import argv
import requests


if __name__ == '__main__':
    if len(argv) < 2:
        val = {'q': ""}
    else:
        val = {'q': argv[1]}

    response = requests.post('http://0.0.0.0:5000/search_user', data=val)
    resp = response.json()
    if response.status_code == 400:
        print('Not a valid JSON')
    else:
        if len(resp) == 0:
            print('No result')
        else:
            id = resp.get('id')
            name = resp.get('name')
            print('[{}] {}'.format(id, name))
