#!/usr/bin/node
const Squares = require('./5-square');
module.exports = class Square extends Squares {
  charPrint (c) {
    if (c === undefined) {
      return this.print();
    } else {
      for (let x = 0; x < this.width; x += 1) {
	console.log(c.repeat(this.height));
      }
    }
  }
};
