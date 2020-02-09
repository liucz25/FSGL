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
    // 可能用不上了
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