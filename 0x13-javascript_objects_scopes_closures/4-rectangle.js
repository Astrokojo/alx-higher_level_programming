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
    for (let step = 0; step < this.height; step++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    [this.width, this.height] = [this.width * 2, this.height * 2];
  }
}
module.exports = Rectangle;
