const express = require('express');
const app = new express();
const { spawn } = require('child_process');
const yf = 'yahooFinance.py'


/*This tells the server to use the client 
folder for all static resources*/
app.use(express.static('client'));

/*This tells the server to allow cross origin references*/
const cors_app = require('cors');
app.use(cors_app());

/*Uncomment the following lines to loan the environment 
variables that you set up in the .env file*/

const dotenv = require('dotenv');
dotenv.config();


//The default endpoint for the webserver
app.get("/", (req, res) => {
    res.render('index.html');
});

//The endpoint for the webserver ending with /url/emotion
app.get("/API", (req, res) => {
    var dataToSend;
    var args = ['-i 1m'];
    args.unshift(yf);
    const python = spawn('python', args);
    python.stdout.on('data', function (data) {
        console.log('Pipe data from python script ...');
        dataToSend = data.toString();
    });

    python.on('close', (code) => {
        console.log('child process close all stdio with code ${code}');
        // send data to browser
        res.send(dataToSend)
    });
});

//The endpoint for the webserver ending with /url/sentiment
app.get("/xxx/xxx", (req, res) => {
    return res.send("url for " + req.query.url);
});


let server = app.listen(8080, () => {
    console.log('Listening', server.address().port)
})

