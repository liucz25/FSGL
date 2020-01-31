var initSqlJs = require('sql.js');
var fs = require('fs');
var path = require('path');

const LocalDB = path.join(__dirname, 'HumanResourcesManager.s3db');

var sqlstr = "select * from RankScore";
/*
// 异步调用
fs.readFile('2.txt', 'utf8', (err, result) => {
    if (err != null) {
        // reject(err)
        console.log("err");
        console.log(err);

    } else {
        // resolve(result);
        console.log("ok");
        console.log(result);
    }
});
// 异步调用变Promise
let getJson = new Promise((resolve, reject) => {
    fs.readFile('1.txt', 'utf8', (err, result) => {
        if (err != null) {
            reject(err)
            console.log("err");

        } else {
            resolve(result);
            console.log("ok");
        }
    });
});

getJson.then(function(resolve) {
    console.log(resolve);
}).catch(function(reject) {
    console.log(reject);
});


*/


/*回调地狱解决？
function p1() {
    return p1 = new Promise(
        (resolve, reject) => {
            initSqlJs((SQL) => {
                resolve(SQL);
            })
        });
}

function p2() {
    return p2 = new Promise(
        (resolve, reject) => {
            var db = new SQL.Database(fb);
            var res = db.exec(sqlstr);
            var resstr = JSON.stringify(res);
            resolve(resstr);

        })

}
p1().then((r1) => {
    console.log(r1);
    return p2()
}).then((r2) => {
    console.log(r2);
});

*/


//then 改成 await 但返回值还是 Promise { <pending> }
var fb = fs.readFileSync(LocalDB);
var sqlstr = "select * from RankScore";
async function get() {
    this.SQL = await initSqlJs();
    var db = new SQL.Database(fb);
    var res = await db.exec(sqlstr);
    var resstr = JSON.stringify(res);
    // console.log(resstr);
    return resstr;

}

async function geta() {
    this.res = await get();
    return res;
}
// get().then((r) => {
//     // console.log(r);
// }); //ok
var res = geta();
console.log(res);