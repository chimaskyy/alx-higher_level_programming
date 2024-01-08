#!/usr/bin/python3
"""
This module sends a request to the URL
displays the body of the response and handles http erro
"""

import sys
import requests

if __name__ == '__main__':
    url = sys.argv[1]

    req = requests.get(url)
    res = req.status_code

    if res >= 400:
        print("Error code: {}".format(res))
    else:
        print(req.text)
