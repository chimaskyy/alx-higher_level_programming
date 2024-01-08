#!/usr/bin/python3

import sys
import urllib.request

req = urllib.request.Request(sys.argv[1])

with urllib.request.urlopen(req) as response:
    request_Id = response.getheader('X-Request-Id')
    print(request_Id)
