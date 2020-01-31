var initSqlJs = require('sql.js');
var fs = require('fs');
var path = require('path');

var sqlstr = "select * from RankScore";

function getJson(sqlstr) {
    const LocalDB = path.join(__dirname, 'HumanResourcesManager.s3db');
    var res = initSqlJs().then(SQL => {
        var fb = fs.readFileSync(LocalDB);
        var db = new SQL.Database(fb);
        var res = db.exec(sqlstr);
        var str = JSON.stringify(res);
        console.log(str);
        var js = JSON.parse(str);
        //    console.log(js.columns);
        //     console.log(js[0].values[1]);
        //     console.log(js[0].values[1][1]);
        return str;

    });
    // console.log("-------------------"+res);
    return res;
};
a = getJson(sqlstr);


// var res = getJson(sqlstr)

console.log(a);