#!/usr/bin/node
const request = require('request');

request('https://jsonplaceholder.typicode.com/todos', function (error, response, body) {
    let users = JSON.parse(body);
    for (let i = 0; i < users.length; i++) {
	console.log(users[i]);
    }
});
