var template = require('art-template');
template.defaults.root = './';
module.exports.data = template('./vm/index.html', { data: 123 });