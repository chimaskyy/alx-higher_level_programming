#!/usr/bin/node
// This script writes to a file

const fs = require('fs');

const fileP = process.argv[2];
const content = process.argv[3];

fs.writeFile(fileP, content, 'utf-8', (error) => {
  if (error) {
    console.log(error);
  }
});
