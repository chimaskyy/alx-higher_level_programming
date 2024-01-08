#!/usr/bin/python3
"""
This module takes your GitHub credentials
(username and password) and uses the GitHub
API to display your id
"""

import sys
import requests

if __name__ == '__main__':

    usr = sys.argv[1]
    paswd = sys.argv[2]
    url = "https://api.github.com/user"

    r = requests.get(url, auth=(usr, paswd))

    if 'id' in r.json():
        print(r.json()['id'])
    else:
        print(None)
