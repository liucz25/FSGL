var initSqlJs = require('sql.js');
var fs = require('fs');
var path = require('path');

const LocalDB = path.join(__dirname, 'rygl.db');

module.exports.getdata = function(sqlstr, call) {
    initSqlJs().then(SQL => {

        var fb = fs.readFileSync(LocalDB);
        var db = new SQL.Database(fb);
        var res = db.exec(sqlstr);
        call(res);
    })
}