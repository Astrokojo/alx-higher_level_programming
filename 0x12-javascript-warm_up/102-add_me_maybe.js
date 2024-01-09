#!/usr/bin/node
function incrementCall (number, theFunction) {
	  theFunction(number + 1);
}
module.exports = { incrementCall };
