#!/bin/bash
#sends a request to url and displays only the status code
curl -sL -w "%{http_code}" "$1" -o /dev/null
