#!/usr/bin/node
const request = require('request');
let count = 0;
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const dict = JSON.parse(body);
    const movies = dict.results;
      for (const [key, values] of Object.entries(movies)) {
	  if (values.characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
              count += 1;
      }
    }
    console.log(count);
  }
});
