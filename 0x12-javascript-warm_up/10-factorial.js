#!/usr/bin/node
function factorial (n) {
  if (isNaN(n)) {
    return 1;
  }
  if (n === 1) {
    return 1;
  }
  return (n * factorial(n - 1));
}
const num = process.argv[2];
const val = factorial(num);
console.log(val);
