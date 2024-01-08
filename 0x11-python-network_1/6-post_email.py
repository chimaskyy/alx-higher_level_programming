#!/usr/bin/python3
"""
This module sends post request to
url and display its body
"""

import sys
import requests

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    data = {
        'email': email
        }
    req = requests.post(url, data=data)
    res = req.text
    print(res)
