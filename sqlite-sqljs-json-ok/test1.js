var initSqlJs = require('sql.js');
var fs = require('fs');
var path = require('path');


const LocalDB = path.join(__dirname, 'HumanResourcesManager.s3db');
var fb = fs.readFileSync(LocalDB);
var db;

initSqlJs().then(SQL => {
    // console.log(SQL);
    db = new SQL.Database(fb);
    var sqlstr = "select * from RankScore";
    var res = db.exec(sqlstr);
    var str = JSON.stringify(res);
    // sconsole.log(str);
    var js = JSON.parse(str);
    // return str;
    // SQL(sstr);
    // [{"columns":["RSid","PersonId","TypeId","TotalScore"],
    // "values":[[1,1,1,null],
    // [2,1,4,null],
    // [3,2,1,null]]}]'
});

function chaxun() {
    return new Promise(function(res, rej) {
        initSqlJs().then((function(SQL) {

            var db = new SQL.Database(fb);
            var sqlstr = "select * from RankScore";
            var resq = db.exec(sqlstr);
            var str = JSON.stringify(resq);
            res(str);
        }))
    })
}
chaxun().then(data => {
    console.log(data)
})