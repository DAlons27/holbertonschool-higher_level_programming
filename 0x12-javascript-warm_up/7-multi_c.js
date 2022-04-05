#!/usr/bin/node
const x = parseInt(process.argv[2], 10);
if (isNaN(x)) {
  console.log('Missing number of occurences');
} else {
  for (let i = 1; i <= x; i += 1) {
    console.log('C is fun');
  }
}
