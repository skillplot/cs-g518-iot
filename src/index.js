import * as spawm from 'child_process';

spawn('python', ['ultrasonic.py']);

python.stdout.on('data', function (data) {
  console.log('Pipe data from python script ...');
  dataToSend = data.toString();
});

// The 'close' event is emitted when the stdio streams of a child process have been closed.
python.on('close', (code) => {
  console.log(`child process close all stdio with code ${code}`);
  // send data to browser
  res.send(dataToSend)
});

