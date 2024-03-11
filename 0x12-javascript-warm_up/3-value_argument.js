#!/usr/bin/node
const ar = process.argv[2];
if (ar === undefined) {
  console.log('No argument');
} else { console.log(ar); }
