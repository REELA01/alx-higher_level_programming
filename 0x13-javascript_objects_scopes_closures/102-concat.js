#!/usr/bin/node
const fl0 = require('fs');
const fl1 = fl0.readFileSync(process.argv[2], 'utf8');
const fl2 = fl0.readFileSync(process.argv[3], 'utf8');
fl0.writeFileSync(process.argv[4], fl1 + fl2);
