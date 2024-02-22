#!/usr/bin/node
// prints the title of a Star Wars movie
// gets the movie id from command line
// the call back function is executed once GET
// request is completed
// erro: prints any error that occurs during the request
// response: contains http obj(status code,header etc)
// body: body of http response i.e data returned
// by the server call to the api
// Parse the response body (which is in JSON
// format) into a JavaScript object

const request = require('request');
const id = process.argv[2];
const endPoint = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(endPoint, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  console.log(data.title);
  // console.log(response.statusCode)
});
