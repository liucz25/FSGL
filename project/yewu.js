const template = require('art-template');
const url = require('url');

const qureystring = require('querystring');
const linkdb = require('./linkdb');
const mansql = require('./mansql');
template.defaults.root = './';
var sqlstr = "select * from person";
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
    editperson_get: function(req, res) {

        var urlobj = url.parse(req.url, true);
        var sqlstr = mansql.table('person').where("PersonID=" + urlobj.query.id).select();
        linkdb.runsql(sqlstr, function(datas) {
            da = mansql.datatojson(datas);
            res.render('./editperson.html', { data: da });
        });
    },
    editperson_post: function(req, res) {

        var data = '';
        req.on('data', function(che) {
            data += che;
        });
        req.on('end', function() {
            var data_obj = qureystring.parse(data);
            var urlobj = url.parse(req.url, true);
            var sqlstr = mansql.where("personID=" + urlobj.query.id).table("person").update(data_obj);
            // console.log(sqlstr);
            linkdb.runsql(sqlstr, function(datas) {
                var backstr = "<script>alert('修改成功');window.location.href='/'</script>";
                res.setHeader('content-type', 'text/html;charset=utf-8');
                // console.log(backstr);
                res.end(backstr);
            })
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
                var backstr = "<script>alert('添加成功');window.location.href='/'</script>";
                res.setHeader('content-type', 'text/html;charset=utf-8');
                // console.log(backstr);
                res.end(backstr);

            })
            res.end();
        });

    }
}