#!/bin/bash
#send JSON post request, JSON file name as second args
curl -X POST -H "Content-type: application/JSON" -d @"$2" "$1"
