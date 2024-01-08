#!/usr/bin/python3
'''This module takes in a URL and an email
sends a POST request to the passed URL with
the email as a parameter, and displays the body
of the response'''

import urllib.request
import sys

url = sys.argv[1]
email = sys.argv[2]

value = {
        'email': email
        }

data = urllib.parse.urlencode(value)
data = data.encode('ascii')

req = urllib.request.Request(url, data)

with urllib.request.urlopen(req) as response:
    content = response.read().decode('utf-8')
    print(content)
