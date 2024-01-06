#!/bin/bash
#sends a GET request to URL, displays the body of the response of 200 status, a header varaible added
curl -sLX GET -H "X-School-User-Id: 98" "$1"
