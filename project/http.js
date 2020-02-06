const express = require('express');
const route = require('./route');

const app = express();


app.engine('html', require('express-art-template')); //express 的模板引擎
app.use(express.static('public')) //使用express托管静态文件
app.use(route); //外部路由



app.listen(8080, function() {
    console.log("请访问127.0.0.1:8080")
});