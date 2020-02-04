var template = require('art-template');
var linkdb = require('./linkdb');
template.defaults.root = './';
var sqlstr = "select * from worktype";

linkdb.getdata(sqlstr, function(datas) {
    module.exports.data = template('./views/nav.html', { data: datas[0] });
    module.exports.data += template('./views/table.html', { data: datas[0] });
})