#!/usr/bin/node
const ar = process.argv[2];
if (isNaN(ar)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + ar);
}
