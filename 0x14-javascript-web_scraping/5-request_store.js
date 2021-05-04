#!/usr/bin/node
const url = process.argv[2];
const filePath = process.argv[3];
const fs = require('fs');
const request = require('request');
let content = '';
request(url, function (response, body, error) {
    if (error) {
	console.error(error);
    } else {
	content = JSON.parse(body);
    }
});

fs.writeFile(filePath, content, 'utf8', function(err) {
    if (err) {
	console.log(err);
    }
});
