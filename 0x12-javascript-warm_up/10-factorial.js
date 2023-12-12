#!/usr/bin/node

// compute and print a factorial

function factorial (n) {
  if (isNaN(n) || n <= 1) {
    return 1;
  }
  return (n * factorial(n - 1));
}
const args = process.argv;
const arg1 = parseInt(args[2]);

console.log(factorial(arg1));
