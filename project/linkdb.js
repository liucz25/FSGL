var initSqlJs = require('sql.js');
var fs = require('fs');
var path = require('path');

const LocalDB = path.join(__dirname, "/../", 'HumanResourcesManager.s3db');

module.exports.getdata = function(call) {
    initSqlJs().then(SQL => {
        var sqlstr = "select * from RankScore";
        var fb = fs.readFileSync(LocalDB);
        var db = new SQL.Database(fb);
        var res = db.exec(sqlstr);
        call(res);
    })
}