#!/usr/bin/node
const arr = process.argv;
if (arr.length < 3) {
  console.log('No argument');
}
if (arr.length === 3) {
  console.log('Argument found');
}
if (arr.length > 3) {
  console.log('Arguments found');
}
