import path from 'path';
import http from 'http';

import cv2 from 'opencv4nodejs-prebuilt'
import express from 'express';
import { Server } from 'socket.io';

import ejs from 'ejs';

import {fileURLToPath} from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);


const app = express();
// Creating Http Server from Express App to work with socket.io
const server = http.Server(app);
// Initializing socket.io object
const io = new Server(server, {
  // Specifying CORS 
  cors: {
    origin: "*",
  }
});

// http://expressjs.com/en/advanced/best-practice-security.html#additional-considerations
app.disable('x-powered-by');


// Require static assets from public folder
app.use(express.static(path.join(__dirname, 'public')));
// Set 'views' directory for any views 
// being rendered res.render()
app.set('views', path.join(__dirname, 'views'));
// app.use(logger);
// app.use(express.static('/static'));
// app.use(express.static(path.join(__dirname, 'views')));


// Set view engine as EJS
app.engine('html', ejs.renderFile);
// app.set('view engine', 'html');
app.set('view engine', 'ejs');

app.get('/', (req, res, next) => {
    res.render('index');
});

const FPS = 100;
const Vcap = new cv2.VideoCapture(0);
Vcap.set(cv2.CAP_PROP_FRAME_WIDTH, 300);
Vcap.set(cv2.CAP_PROP_FRAME_HEIGHT, 300);

setInterval(() => {
    const frame = Vcap.read();
    const image = cv2.imencode('.jpg', frame).toString('base64');
    io.emit('image', image);
}, 1000 / FPS);

server.listen(3030, () => console.log('narenltk says open up your browser'));

