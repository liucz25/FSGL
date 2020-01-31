var initSqlJs = require('sql.js');
var fs = require('fs');
var path = require('path');

const LocalDB = path.join(__dirname, 'HumanResourcesManager.s3db');

var sqlstr = "select * from RankScore";

// resstr = 'null';
// initSqlJs().then(SQL => {
//     // console.log(SQL);
//     var fb = fs.readFileSync(LocalDB);
//     var db = new SQL.Database(fb);
//     var res = db.exec(sqlstr);
//     global.resstr = JSON.stringify(res);
//     // console.log(resstr);
// })

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