#!/usr/bin/node

// increments and calls a function

function addMeMaybe (number, theFunction) {
  return theFunction(number + 1);
}
exports.addMeMaybe = addMeMaybe;
