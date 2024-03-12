#!/usr/bin/node
const dic = require('./101-data').dict;
const tlist = Object.entries(dic);
const va = Object.values(dic);
const vaUniq = [...new Set(va)];
const nDic = {};
for (const j in vaUniq) {
  const list = [];
  for (const k in tlist) {
    if (tlist[k][1] === vaUniq[j]) {
      list.unshift(tlist[k][0]);
    }
  }
  nDic[vaUniq[j]] = list;
}
console.log(nDic);
