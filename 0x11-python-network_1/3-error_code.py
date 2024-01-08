#!/usr/bin/python3
'''This module sends a request to the URL
displays the body of the response and handles http erro'''

import sys
from urllib import request, error

url = sys.argv[1]

req = request.Request(url)
try:
    with request.urlopen(req) as response:
        data = response.read().decode('utf-8')
        print(data)
except error.HTTPError as err:
    print("Error code: {}".format(err.code))
