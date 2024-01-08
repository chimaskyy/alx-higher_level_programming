#!/usr/bin/python3
'''This module fetches the url
"https://alx-intranet.hbtn.io/status" '''

import urllib.request

req = urllib.request.Request('https://alx-intranet.hbtn.io/status')

with urllib.request.urlopen(req) as response:
    data = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(data)))
    print("\t- content: {}".format(data))
    print("\t- utf8 content: {}".format(data.decode('utf-8')))
