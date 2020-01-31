var initSqlJs = require('sql.js');
var fs = require('fs');
const template = require('art-template');
const path = require('path');

const views = path.join(__dirname, 'views', 'index.art')
const LocalDB = path.join(__dirname, 'HumanResourcesManager.s3db');
var sqlstr = "select * from RankScore";

//then 改成 await 但返回值还是 Promise { <pending> }
var fb = fs.readFileSync(LocalDB);
var sqlstr = "select * from RankScore";
async function get() {
    this.SQL = await initSqlJs();
    var db = new SQL.Database(fb);
    var res = await db.exec(sqlstr);
    var resstr = JSON.stringify(res);
    // console.log(res[0].columns);
    // return resstr;
    // result = [{
    //     name: '暂时',
    //     age: 20,
    //     sex: '男'
    // }, {
    //     name: 'asdf',
    //     age: 20,
    //     sex: 'nv'
    // }, {
    //     name: 'asf',
    //     age: 45,
    //     sex: "asf"
    // }]



    // users: [{
    //     name: '暂时',
    //     age: 20,
    //     sex: '男'
    // }, {
    //     name: 'asdf',
    //     age: 20,
    //     sex: 'nv'
    // }, {
    //     name: 'asf',
    //     age: 45,
    //     sex: "asf"
    // }]


    const html = template(views, {
        data: res[0]
    });
    console.log(html);
}
get();