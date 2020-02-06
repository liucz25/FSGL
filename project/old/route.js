var yewu = require('./yewu');
var fs = require('fs')
module.exports.bind = function(server) {
    server.on('request', function(request, response) {
        var urls = request.url;
        if (urls == '/') {
            // console.log(yewu.data);
            // return;
            response.end(yewu.data);
        } else {
            fs.readFile('.' + urls, function(err, data) {
                response.end(data);
            })
        }

    })
}