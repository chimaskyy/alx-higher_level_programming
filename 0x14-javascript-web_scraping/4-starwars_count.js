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
const id = '18';
const endPoint = process.argv[2];
let count = 0;

request.get(endPoint, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  data.results.forEach((film) => {
    film.characters.forEach((character) => {
      if (character.includes(id)) {
        count += 1;
      }
    });
  });
  console.log(count);
});
