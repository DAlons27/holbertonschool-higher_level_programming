#!/usr/bin/node
let counts = 0;

exports.logMe = function (item) {
  console.log(counts + ': ' + item);
  counts++;
};
