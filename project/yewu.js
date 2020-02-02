var template = require('art-template');
var linkdb = require('./linkdb');
template.defaults.root = './';

linkdb.getdata(function(datas) {
    module.exports.data = template('./vm/index.html', { data: datas[0] });
})