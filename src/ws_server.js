import WebSocket from 'ws';

import appcfg from './app/config/settings.js';
import { uuidv4 } from './app/common.js';

const port = process.env.PORT || appcfg.port;

const wss = new WebSocket.Server({
  port: port
  // // Other options settable:
  // clientNoContextTakeover: true, // Defaults to negotiated value.
  // serverNoContextTakeover: true, // Defaults to negotiated value.
  // serverMaxWindowBits: 10, // Defaults to negotiated value.
  // // Below options specified as default values.
  // concurrencyLimit: 10, // Limits zlib concurrency for perf.
  // threshold: 1024 // Size (in bytes) below which messages
  // // should not be compressed if context takeover is disabled.
});
// const { createServer } = require('http');
// const server = createServer(app);
// const wss = new WebSocketServer({ server });

wss.onerror = function () {
  console.log("Some Error occurred");
}


const clients = new Map();

function heartbeat() {
  this.isAlive = true;
}

function broadcast(data) {
  wss.clients.forEach(ws => {
    ws.send(data, () => {});
  });
};

function ping(data) {
  wss.clients.forEach(ws => {
    if (ws.isAlive === false) return ws.terminate();

    ws.isAlive = false;
    ws.ping();
  });
};


wss.on('connection', (ws, req, client) => {
  try {

    ws.isAlive = true;
    ws.on('pong', heartbeat);

    console.log('Client connected');
    const ip = req.socket.remoteAddress;
    // const ip = req.headers['x-forwarded-for'].split(',')[0].trim();


    const id = uuidv4();
    const color = Math.floor(Math.random() * 360);
    let memory = process.memoryUsage();
    let cpuUsage = process.cpuUsage();
    const metadata = {
      id,
      color,
      memory,
      cpuUsage,
    };

    clients.set(ws, metadata);

    ws.on("message", (data) => {
      console.log(`Received message ${data} from user ${client}`);
      console.log(`${data}`);
    });

    const interval = setInterval(() => {
      metadata.memory = process.memoryUsage(metadata.memory);
      metadata.cpuUsage = process.cpuUsage(metadata.cpuUsage);
      ws.send(JSON.stringify(metadata), () => {
        //ignore error
      });
    }, 1000);
    console.log('started client interval');

    wss.on("close", () => {
      console.log("Client disconnected");
      clearInterval(interval);
    });
  } catch(e) {
    console.error(e.message);
  }
});

console.log('Server is running on port', port);
