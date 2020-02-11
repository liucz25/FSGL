module.exports = {
    wh: undefined,
    tb: undefined,
    where: function(wh) {
        this.wh = wh;
        return this;
    },
    table: function(table) {
        this.tb = table;
        return this;
    },
    select: function() {
        if (table = undefined) {
            return "请输入表名，qingshurubiaoming";
        } else {
            if (wh = undefined) {
                var sqlstr = "select * from " + this.tb;
            } else {
                var sqlstr = "select * from  " + this.tb + " where " + this.wh;
            }
        }
        this.tb = undefined;
        this.wh = undefined;
        return sqlstr;
    },
    insert: function(data) {
        if (table = undefined) {
            var sqlstr = "select * from "
        } else {
            var sqlstr = "insert into  " + this.tb + ' ' + data;
            this.tb = undefined;
            return sqlstr;
        }
    },
    update: function(data) {
        var set = '';
        for (i in data) {
            set += (i + "='" + data[i] + "',");
        }
        set = set.slice(0, set.length - 1);
        if (table = undefined) {
            return "请输入表名，qingshurubiaoming";
        } else {

            var sql = "update " + this.tb + " set " + set + ' where ' + this.wh;
        }
        // console.log(sql);
        this.tb = undefined;
        return sql;
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
    },
    datatojson: function(data) {
        var js = "{"
        for (i in (data[0].values)[0]) {

            js += '"' + data[0].columns[i] + '":"' + data[0].values[0][i] + '",';


        }
        js = js.slice(0, js.length - 1);
        js += "}";
        // console.log(js);
        var jsn = JSON.parse(js);
        // console.log(jsn);
        // data = column.slice(0, column.length - 1) + ')' + values.slice(0, values.length - 1) + ');';
        return jsn;
    }
}