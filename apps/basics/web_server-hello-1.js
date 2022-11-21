// ## Copyright (c) 2022 mangalbhaskar. All Rights Reserved.
const __author__ = 'mangalbhaskar'

import express from 'express';
import appcfg from './app/config/settings.js';

var app = express();


app.get('/', function(req, res) {
  res.send('Hello World!');
});


app.get('/hello', function(req, res) {
  res.json({"message":"Hello World...!!"});
});


app.get('/hello/blah', function(req, res) {
  res.json({"message":"Hello blah!!"});
});


app.get('/hello/:name', function(req, res) {
  var name = req.params.name; //or use req.param('id')
  // var id2 = req.query.id; 
  res.json({"message":`Hello ${name}!`});
});


app.get('/hello/:name/age/:age', function(req, res) {
  var name = req.params.name;
  var age = parseInt(req.params.age);
  res.json({"message":`Hello ${name}, your age is ${age}!`});
});


app.get('/dnnarch', function(req, res) {
  res.send('Coming Soon...');
})

app.listen(appcfg, function() {
  console.log(`Example app listening on port ${appcfg.port}!`)
});

