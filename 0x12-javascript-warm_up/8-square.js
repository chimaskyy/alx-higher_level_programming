#!/usr/bin/node

// prints a square

const args = process.argv;
let i, j;
const size = parseInt(args[2]);
let row;

if (Number.isInteger(size)) {
  for (i = 0; i < size; i++) {
    // accumulate 'X'
    row = '';
    for (j = 0; j < size; j++) {
      // append 'X' for each column in the row
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
