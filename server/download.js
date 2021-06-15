var fs = require('fs');
var express = require('express');
var app = express();
var http = require('http');


var server = http.createServer(app).listen(3303,function()){
console.log('Server Running . ')};


app.get('/',function(req,res){
    fs.readFile('index.html',function(error,data){
        res.writeHead(200,{'Content-Type':'text/html'});
        res.end(data);



    });
});


app.get('/download/:id',function(req,res){
        var filename = req.params.id;
        filepath=__dirname + "/files/"+filename;
        res.download(filepath);
});