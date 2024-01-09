#!/usr/bin/node
const firstArg = process.argv[2];
if (!parseInt(firstArg)){
	console.log("Not a number")
} else {
	console.log(`My number: ${firstArg}`);
}
