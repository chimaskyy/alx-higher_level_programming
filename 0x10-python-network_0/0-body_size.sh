#!/bin/bash
# takes in a URL, sends a request to it and displays size of body
curl -sI "$1" | grep -i 'Content-Length' | awk '{print $2}'
