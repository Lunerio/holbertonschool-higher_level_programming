#!/usr/bin/node

const Squares = require('./5-square');

module.exports = class Square extends Squares {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let char = c;
    if (c === undefined) {
      char = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(char.repeat(this.width));
    }
  }
};
