#!/usr/bin/node
const ar = process.argv.length - 2;
if (ar === 0) {
  console.log('No argument');
} else if (ar === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
