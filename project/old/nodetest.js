var http = require('http');
var route = require('./route');
var server = http.createServer();
server.on('request',function(req,res){
    res.write("<h1>node test<h1>");
    res.end();
    });
server.listen('8080', function() {
    console.log("请访问 127.0.0.1:8080");
})
