#!/usr/bin/node
const ar = process.argv[2];
if (isNaN(ar)) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < ar; i++) { console.log('C is fun'); }
}
