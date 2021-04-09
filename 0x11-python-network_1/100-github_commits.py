#!/usr/bin/python3
""" This module uses requests to get information from a user
    from GITHUB API
"""


from sys import argv
import requests


if __name__ == '__main__':
    # first the owner and then the repo
    url = "https://api.github.com/repos/" + argv[2] + '/' + argv[1] + '/commits'
    response = requests.get(url)
    dict = response.json() # is a list
    count = 0
    for element in dict:
        if count == 11:
            break
        sha_value = element.get('sha') # this
        commit = element.get('commit')
        author = commit.get('author')
        name = author.get('name') # this
        print('{}: {}'.format(sha_value, name))
        count += 1
