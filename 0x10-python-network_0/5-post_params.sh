#!/bin/bash
#sends a POST request to URL, displays the body of the response of 200 status, pass variables with value
curl -sLX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
