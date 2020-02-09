var template = require('art-template');


var linkdb = require('./linkdb');
template.defaults.root = './';
var sqlstr = "select * from personworkload";
var sqlstr1 = "select * from workload";

module.exports = {
    getall: function(req, res) {
        linkdb.getdata(sqlstr, function(datas) {
            var html = template('./views/index.html', { data: datas[0] });
            html += template('./views/table.html', { data: datas[0] });
            res.end(html);
        })
    },
    getone: function(req, res) {
        linkdb.getdata(sqlstr1, function(datas) {
            res.render('./table.html', { data: datas[0] }); //express 框架的render方法
        })
    },
    addperson: function(req, res) {
        res.render('./addperson.html');
    },
    update: function(req, res) {

        console.log(require('querystring').parse(req));
        res.end("req");

    }
}