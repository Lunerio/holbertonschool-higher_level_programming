#!/usr/bin/node
const argLen = (process.argv.length) - 2;
if (argLen === 0 || argLen === 1) {
  console.log(0);
} else {
  const prev = process.argv;
  prev.sort(function (a, b) { return a - b; });
  console.log(prev[prev.length - 2]);
}
