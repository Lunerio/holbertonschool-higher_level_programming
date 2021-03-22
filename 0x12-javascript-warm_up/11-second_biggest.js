#!/usr/bin/node
const argLen = (process.argv.length) - 2;
if (argLen === 0 || argLen === 1) {
  console.log(0);
} else {
  let biggest = parseInt(process.argv[2]);
  let prev = parseInt(process.argv[2]);
  for (let i = 2; i < process.argv.length; i++) {
    if (parseInt(process.argv[i]) > biggest) {
      prev = biggest;
      biggest = parseInt(process.argv[i]);
    }
  }
  console.log(prev);
}
