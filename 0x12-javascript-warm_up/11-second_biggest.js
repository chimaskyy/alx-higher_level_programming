#!/usr/bin/node

// Search second largest number

const args = process.argv;
const len = args.length;
let largest;
let secondLargest;
let curNum, i;

if (len < 4) {
  console.log('0');
} else {
  largest = parseInt(args[2]);
  secondLargest = parseInt(args[3]);

  for (i = 3; i < len; i++) {
    curNum = parseInt(args[i]);

    if (curNum > largest) {
      secondLargest = largest;
      largest = curNum;
    } else if (curNum > secondLargest) {
      secondLargest = curNum;
    }
  }

  console.log(secondLargest);
}
