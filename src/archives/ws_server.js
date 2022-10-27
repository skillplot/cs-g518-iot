// ## Copyright (c) 2020 mangalbhaskar. All Rights Reserved.
const __author__ = 'mangalbhaskar'

const WebSocket = require('ws')
const appcfg = require('./app/config/settings');

const socket = new WebSocket.Server({ port: appcfg.port })

// connection established,
socket.onopen = function(event) {
  console.log("[open] Connection established");
  console.log("Sending to server");
  socket.send("My name is John");
}

// data received
socket.onmessage = function(event) {
  console.log(`[message] Data received from server: ${event.data}`);
}

// websocket error
socket.onerror = function(event) {
  if (event.wasClean) {
    console.log(`[close] Connection closed cleanly, code=${event.code} reason=${event.reason}`);
  } else {
    // e.g. server process killed or network down
    // event.code is usually 1006 in this case
    console.log('[close] Connection died');
  }
}

// connection closed
socket.onclose = function(event) {
  console.log(`[error] ${error.message}`);
}
