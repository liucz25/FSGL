var http = require('http');
http.createServer(function handler(req, res) {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello World!!!\n');
}).listen(8006, "0.0.0.0");
console.log('Server runing at http://127.0.0.1:1337/');