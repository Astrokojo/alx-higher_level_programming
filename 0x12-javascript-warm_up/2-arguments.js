#!/usr/bin/node
const func = process.argv.length
if (func === 2){
	console.log("No argument");
} else if (func === 3){
	console.log("Argument found");
} else {
	console.log("Arguments found");
};
