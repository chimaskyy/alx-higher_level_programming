#!/usr/bin/node

//  prints x times “C is fun”

const args = process.argv;
let i;

if (Number.isInteger(parseInt(args[2]))) {
  for (i = 0; i < args[2]; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
