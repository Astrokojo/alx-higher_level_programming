#!/usr/bin/node
exports.incrementCall = function (number, theFunction) {
	number++;
	theFunction(number);
};
