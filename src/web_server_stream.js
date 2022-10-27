// ## Copyright (c) 2022 mangalbhaskar. All Rights Reserved.
const __author__ = 'mangalbhaskar'

import express from 'express';
import appcfg from './app/config/settings.js';

var app = express();


app.get('/', function(req, res) {
  res.json({"message":"Streaming server using NodeJs"});
});


app.get('/video', function(req, res) {
  res.send('Coming Soon...');
});


app.get('/cam', function(req, res) {
  res.send('Coming Soon...');
});


app.listen(appcfg, function() {
  console.log(`Example app listening on port ${appcfg.PORT}!`)
});

