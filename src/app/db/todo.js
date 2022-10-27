var mongoose = require('mongoose');
var dbstr = 'mongodb://localhost:27017/todoapp';

mongoose.connect(dbstr);

var schema = new mongoose.Schema({
  name: String
  ,completed: Boolean
  ,note: String
  ,updated_at: {
    type: Date
    ,default: Date.now
  }
});

var Todo = mongoose.model(
  'Todo'
  ,schema
);

// Create a todo in memory
var todo = new Todo({
  name: 'Master NodeJS'
  ,completed: false
  ,note: 'Getting there...'
});

// Save it to database
todo.save(function(err){
  if(err)
    console.log(err);
  else
    console.log(todo);
});

Todo.create({
    name: 'Create something with Mongoose'
    ,completed: true
    ,note: 'this is one'
  }, function(err, todo) {
    if(err) console.log(err);
    else console.log(todo);
});
