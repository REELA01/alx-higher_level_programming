#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((cnt, current) => current === searchElement
    ? cnt + 1
    : cnt, 0
  );
};
