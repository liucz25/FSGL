var http = require('http');
var route = require('./route');
var server = http.createServer();
route.bind(server);
server.listen('8080', function() {
    console.log("请访问 127.0.0.1:8080");
})