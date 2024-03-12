#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let ix = 0; ix < this.height; ix++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const curr = this.width;
    this.width = this.height;
    this.height = curr;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
