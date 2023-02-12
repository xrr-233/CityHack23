const express = require('express');
const app = new express();
const { spawn } = require('child_process');


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


//The endpoint 
app.get("/DNN", (req, res) => {
    var dataToSend;
    const python = spawn('python', ['DNN.py']);
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

//The endpoint 
app.get("/SMA", (req, res) => {
    var dataToSend;
    const python = spawn('python', ['SMA.py']);
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

app.get("/OLS", (req, res) => {
    var dataToSend;
    const python = spawn('python', ['OLS.py']);
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

app.get("/SVM", (req, res) => {
    var dataToSend;
    const python = spawn('python', ['SVM.py']);
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


let server = app.listen(8080, () => {
    console.log('Listening', server.address().port)
})

