#!/usr/bin/node
const { list } = require('./100-data');
const listB = list.map((i, index) => {
  return i * index;
});
console.log(list);
console.log(listB);
