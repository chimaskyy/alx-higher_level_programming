#!/usr/bin/node

//  executes x times a function

function callMeMoby (x, theFunction) {
  let i;

  for (i = 0; i < x; i++) {
    theFunction();
  }
}
exports.callMeMoby = callMeMoby;
