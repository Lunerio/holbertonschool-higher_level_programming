#!/usr/bin/node
const height = parseInt(process.argv[2]);
if (isNaN(height)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < height; i++) {
    console.log('X'.repeat(height));
  }
}
