#!/usr/bin/node
let file_path = process.argv[2]
fs = require('fs')
fs.readFile(file_path, 'utf8', function (err,data) {
    if (err) {
	return console.log(err);
    }
    console.log(data);
});
