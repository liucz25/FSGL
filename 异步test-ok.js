var initSqlJs = require('sql.js');
var fs = require('fs');
var path = require('path');

const LocalDB = path.join(__dirname, 'HumanResourcesManager.s3db');

var sqlstr = "select * from RankScore";

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