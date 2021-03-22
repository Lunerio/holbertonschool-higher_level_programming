#!/usr/bin/node
function add (a, b) {
  const val = a + b;
  return val;
}
const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);
const value = add(a, b);
console.log(value);
