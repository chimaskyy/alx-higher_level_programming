#!/usr/bin/node
//This script writes to a file


const fs = require('fs');

const file_p = process.argv[2];
const content = process.argv[3] + '\n';

try {
	fs.writeFileSync(file_p, content, 'utf-8');
}
catch (e) {
	console.log(e);
}

