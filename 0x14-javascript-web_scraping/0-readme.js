#!/usr/bin/node
// This script that reads and prints the content of a file.

const fs = require('fs');

const file_ = process.argv[2];

try {
  const content = fs.readFileSync(file_, 'utf-8');
  console.log(content);
} catch (e) {
  console.log(e);
}
