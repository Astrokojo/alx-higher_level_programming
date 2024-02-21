#!/usr/bin/node
const fs = require('node:fs');
const filename = process.argv[2];
const data = process.argv[3];
fs.writeFile(filename, data, 'utf8', (err) => {
  if (err) throw err;
  console.log(data);
});
