#!/usr/bin/node

const x = parseInt(process.argv[2], 10);
if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i += 1) {
    console.log('X'.repeat(x));
  }
}
