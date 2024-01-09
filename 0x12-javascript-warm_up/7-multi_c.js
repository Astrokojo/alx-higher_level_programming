#!/usr/bin/node
const numArg = parseInt(process.argv[2]);

if (isNaN(numArg)) {
  console.log('Missing number of occurrences');
} else {
  for (let step = 0; step < numArg; step++) {
    console.log('C is fun');
  }
}
