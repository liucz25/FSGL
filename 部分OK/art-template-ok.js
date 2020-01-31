const template = require('art-template');
const path = require('path');

console.log(__dirname);
const views = path.join(__dirname, 'view.art')

const html = template(views, {
    data: {
        name: '张三',
        age: 20
    }
});

console.log(html);