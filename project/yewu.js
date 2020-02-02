var template = require('art-template');
var linkdb = require('./linkdb');
template.defaults.root = './';
var sqlstr = "select * from RankScore";

linkdb.getdata(sqlstr, function(datas) {
    module.exports.data = template('./vm/index.html', { data: datas[0] });
})