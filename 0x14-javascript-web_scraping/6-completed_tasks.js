#!/usr/bin/node
const request = require('request');

request('https://jsonplaceholder.typicode.com/todos', function (error, response, body) {
    let tasks = JSON.parse(body);
    for (let i = 0; i < tasks.length; i++) {
	console.log(tasks[i].title);
    }
});
