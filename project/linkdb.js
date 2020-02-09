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
    update: function(data) {
        var set = '';
        for (i in data) {
            set += (i + "='" + data[i] + "',");
        }
        set = set.slice(0, set.length - 1);
        var sql = "updata users set " + set + ' where ' + this.wh;

        console.log(sql);

    },
    insert: function(data) {
        var set = '';
        for (i in data) {
            set += (i + "='" + data[i] + "',");
        }
        set = set.slice(0, set.length - 1);
        var sql = "insert into person " + set;
        console.log(sql);
        // var fb = fs.readFileSync(LocalDB);
        // var db = new SQL.Database(fb);
        // var res = db.exec(sqlstr);



    },
    where: function(wh) {
        this.wh = wh;
        return this;
    },
    select: function() {
        if (wh = undefined) {
            var sqlstr = "select * from "
        } else {
            var sqlstr = "select * from     where " + this.wh;
        }
        this.wh = undefined;




    }

}