var initSqlJs = require('sql.js');
var fs = require('fs');
var path = require('path');

const LocalDB = path.join(__dirname, 'HumanResourcesManager.s3db');
initSqlJs().then(SQL => {

    var fb = fs.readFileSync(LocalDB);

    var db = new SQL.Database(fb);

    var sqlstr = "select * from RankScore";
    var res = db.exec(sqlstr);
    var str = JSON.stringify(res);
    console.log(str);
    var js = JSON.parse(str);
    console.log(js.columns);
    //     console.log(js[0].values[1]);
    //     console.log(js[0].values[1][1]);
    return str;
    // [{"columns":["RSid","PersonId","TypeId","TotalScore"],
    // "values":[[1,1,1,null],
    // [2,1,4,null],
    // [3,2,1,null]]}]'
});