const db = require('./mandb');
var initSqlJs = require('sql.js');
var fs = require('fs');
var path = require('path');
const LocalDB = path.join(__dirname, 'rygl.db');
module.exports = {
    getdata: function(sqlstr, call) {
        initSqlJs().then(SQL => {

            var fb = fs.readFileSync(LocalDB);
            var db = new SQL.Database(fb);
            var res = db.exec(sqlstr);
            call(res);
        })
    },
    runsql: function(sqlstr, call) {
        initSqlJs().then(SQL => {

            var fb = fs.readFileSync(LocalDB);
            var db = new SQL.Database(fb);
            var res = db.exec(sqlstr);
            var data = db.export();
            var buffer = new Buffer(data);
            fs.writeFileSync(LocalDB, buffer);


            call(res);
        })
    },
    update: function(data) {
        var set = '';
        for (i in data) {
            set += (i + "='" + data[i] + "',");
        }
        set = set.slice(0, set.length - 1);
        var sql = "updata users set " + set + ' where ' + this.wh;

        console.log(sql);

    },
    dataformat: function(data) {
        var column = '(';
        var values = 'VALUES (';
        for (i in data) {
            column += i + ',';
            values += "'" + data[i] + "'" + ','
        }
        data = column.slice(0, column.length - 1) + ')' + values.slice(0, values.length - 1) + ');';
        return data;
    }
}