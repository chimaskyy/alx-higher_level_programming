#!/bin/bash
#displays all HTTP methods the server will accept.
curl -sILX OPTIONS "$1" | grep -i Allow | awk -F ": " '{print $2}'
