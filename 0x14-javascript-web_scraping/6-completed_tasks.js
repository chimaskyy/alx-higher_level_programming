#!/usr/bin/node
//

const request = require('request');
const endPoint = process.argv[2];

request.get(endPoint, (error, response, body) => {
  if (error) {
    console.log(error);
  }

  // Parse response body (in JSON format) into a JavaScript object
  const todos = JSON.parse(body);

  const taskCompleted = {};

  // Iterate through each 'todo' item in the response body
  todos.forEach((todo) => {
    // Check if the 'completed' property of the 'todo' is true
    if (todo.completed) {
      if (!taskCompleted[todo.userId]) {
        taskCompleted[todo.userId] = 1;
      } else {
        taskCompleted[todo.userId] += 1;
      }
    }
  });
  console.log(taskCompleted);
});
