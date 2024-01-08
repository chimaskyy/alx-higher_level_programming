#!/usr/bin/python3
'''This module fetches the url
display the value of a variable X-Request_Id '''

import requests
import sys

url = sys.argv[1]

req = requests.get(url)
data = req.headers['X-Request-Id']
print(data)
