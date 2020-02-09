var initSqlJs = require('sql.js');
var fs = require('fs');
var path = require('path');

const LocalDB = path.join(__dirname, 'rygl.db');
module.exports = {
    wh: undefined,
    table: undefined,
    where: function(wh) {
        this.wh = wh;
        return this;
    },
    table: function(table) {
        this.table = table;
        return this;
    },
    select: function() {
        if (wh = undefined) {
            var sqlstr = "select * from "
        } else {
            var sqlstr = "select * from     where " + this.wh;
        }
        this.wh = undefined;
    },
    insert: function(data) {
        if (table = undefined) {
            var sqlstr = "select * from "
        } else {
            var sqlstr = "insert into  " + this.table + ' ' + data;
            return sqlstr;
        }
        this.table = undefined;
    },
}