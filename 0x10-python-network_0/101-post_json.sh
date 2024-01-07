#!/bin/bash
#send JSON post request, JSON file name as second args
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
