#!/usr/bin/node
const square = require('./5-square');
class Square extends square {
	constructor (size) {
		super(size);
	}
	charPrint (c) {
		if (c === undefined) {
			c = 'X';
		} else {
			for (let step = 0; step < this.height; step++) { console.log(c.repeat(this.width));
			}
		}
	}
}
module.exports = Square;
