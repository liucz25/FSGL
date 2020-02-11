const template = require('art-template');
const url = require('url');

const qureystring = require('querystring');
const linkdb = require('./linkdb');
const mansql = require('./mansql');
template.defaults.root = './';
var sqlstr = "select * from worktype";
var sqlstr1 = "select * from workload";

module.exports = {
    getall: function(req, res) {
        linkdb.getdata(sqlstr, function(datas) {
            // var html = template('./views/index.html', { data: datas[0] });
            var html = template('./views/persontable.html', { data: datas[0] });
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
    editperson: function(req, res) {
        res.render('./editperson.html', {
            data: {
                id: 22,
                name: 'sadfa',
                age: 11
            }
        });
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
            var sqlstr = mansql.where("id=" + urlobj.query.id).update(data_obj);
            linkdb.runsql(sqlstr, function(datas) {
                res.end(data);
            })
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
            var insert_data = mansql.dataformat(data_obj);
            var sqlstr = mansql.table("person").insert(insert_data);
            // console.log(sqlstr);

            linkdb.runsql(sqlstr, function(datas) {
                res.end(data);
            })
            res.end();
        });

    }
}