#!/usr/bin/node
exports.converter = function (base) {
  return numb => numb.toString(base);
};
