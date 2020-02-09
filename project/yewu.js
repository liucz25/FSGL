var template = require('art-template');
const url = require('url');

const qureystring = require('querystring');

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
    update_get: function(req, res) {
        // console.log(require('querystring').parse(req));
        res.end("require('querystring').parse(req)");
    },
    update_post: function(req, res) {
        var data = '';
        req.on('data', function(che) {
            data += che;
        });
        req.on('end', function() {
            var data_obj = qureystring.parse(data);
            console.log(data_obj);
            var urlobj = url.parse(req.url, true);
            linkdb.where("id=" + urlobj.query.id).update(data_obj);
            res.end();
        });
    },
    insert_post: function(req, res) {

        var data = '';
        req.on('data', function(che) {
            data += che;
        });
        req.on('end', function() {
            var data_obj = qureystring.parse(data);
            sqlstr = linkdb.insert(data_obj);
            linkdb.runsql(sqlstr, function(datas) {
                res.end(data);
            })
            res.end();
        });

    }
}