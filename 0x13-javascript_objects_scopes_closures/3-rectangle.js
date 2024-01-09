#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;

    if (w <= 0 || h <= 0) {
      return Rectangle;
    }
  }

  print () {
    for (let step = 0; step < this.height; step++) { console.log('X'.repeat(this.width)); }
  }
}
module.exports = Rectangle;
