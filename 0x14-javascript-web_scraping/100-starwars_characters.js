#!/usr/bin/node

const reqq = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';
reqq.get(url + id, function (error, res, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  const dd = data.characters;
  for (const i of dd) {
    reqq.get(i, function (error, res, body_1) {
      if (error) {
        console.log(error);
      }
      const data_1 = JSON.parse(body_1);
      console.log(data_1.name);
    });
  }
});
