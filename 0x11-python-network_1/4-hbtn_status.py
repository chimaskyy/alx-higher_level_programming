#!/usr/bin/python3
'''This module fetches the url
"https://alx-intranet.hbtn.io/status" '''

import requests

req = requests.get('https://alx-intranet.hbtn.io/status')
res = req.text
print("Body response:")
print("\t- type: {}".format(type(res)))
print("\t- content: {}".format(res))
