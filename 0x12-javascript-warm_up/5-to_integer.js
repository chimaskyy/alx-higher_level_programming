#!/usr/bin/node

/*  prints My number: <first argument converted in integer> if the first argumen
 can be converted to an integer
 */

const args = process.argv;

if (Number.isInteger(parseInt(args[2]))) {
  console.log('My number: ' + args[2]);
} else {
  console.log('Not a number');
}
