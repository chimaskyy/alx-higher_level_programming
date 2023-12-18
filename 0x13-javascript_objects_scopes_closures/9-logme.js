#!/usr/bin/node

// print number of args

let numOfCall = 0;
exports.logMe = function (item) {
  const { log } = console;

  log(`${numOfCall}: ${item}`);
  numOfCall++;
};
