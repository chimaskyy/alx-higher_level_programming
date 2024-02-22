#!/usr/bin/node
// This script displays status code of a GET request

const request = require('request');
const url_ = process.argv[2];

request.get(url_, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
