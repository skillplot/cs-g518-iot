import WebSocket from 'ws';

import appcfg from './app/config/settings.js';

const port = process.env.PORT || appcfg.port;
const url = `ws://localhost:${port}`

const ws = new WebSocket(url)

function heartbeat() {
  clearTimeout(this.pingTimeout);
  // Use `WebSocket#terminate()`, which immediately destroys the connection,
  // instead of `WebSocket#close()`, which waits for the close timer.
  // Delay should be equal to the interval at which your server
  // sends out pings plus a conservative assumption of the latency.
  this.pingTimeout = setTimeout(() => {
    this.terminate();
  }, 30000 + 1000);
}

function genBinaryData() {
  const array = new Float32Array(5);

  for (var i = 0; i < array.length; ++i) {
    array[i] = i / 2;
  }
  return array;
}

ws.on('open', function open() {
  ws.send('something');
  ws.send(genBinaryData());
});

ws.on('message', function message(data) {
  console.log(`${data}`);
  // ws.send(JSON.stringify(data));
});

// ws.on("stream", function(data) {
//   console.log(`${data}`);
//   if (data.frame) {
//     var img = new Image();
//     const src = 'data:image/jpeg;base64,' + data.frame.buffer;
//   }
// });


ws.on('stream', async (data) => {
    const buffer = Buffer.from(data.frame, 'base64');
    await fs.writeFile('logs', buffer).catch(console.error); // fs.promises
});

ws.on('open', heartbeat);
ws.on('ping', heartbeat);
ws.on('close', function clear() {
  clearTimeout(this.pingTimeout);
});
// ws.onerror = (error) => {
//   console.log(`WebSocket error: ${error}`)
// }