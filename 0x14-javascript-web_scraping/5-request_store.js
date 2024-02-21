#!/usr/bin/node
const fs = require('node:fs');
const request = require('request');
const url = process.argv[2];
const file_path = process.argv[3];
request(url).pipe(fs.createWriteStream(file_path));
