<template>
    <div>
        <el-button @click="getData">获取数据</el-button>
        <el-button @click="insertData">插入数据</el-button>
        <el-button @click="updateData">修改数据</el-button>
        <el-button @click="delData">删除数据</el-button>
    </div>
</template>
<script>
export default {
    name:'LowdbTest',
    methods:{
        getData(){
            this.mydb('db') //访问挂载在Vue上的mydb方法，并将json文件名‘db’传给该方法
            let data=this.mydb('db').get('RECORDS').find({uid:2}).value();//找到项目的 public下的db.json文件中的，RECORDS下的，字段uid为2的对象;
            console.log(data); // {uid: 2, user: {…}}uid: 2user: {name: "typicode", age: 18}__proto__: Object
        },
        insertData(){
           // 给项目中 public下的db.json文件的RECORDS数组新增一个元素
            this.mydb('db').get('RECORDS').push({ uid: 4, name: 'xxx', info: '新纪录' }).write();
            // push成功后可以查看到，db.json中多了一个比之前多了一个 { uid: 4, name: 'xxx', info: '新纪录' }
        },
        updateData(){
            // 找到db.json里RECORDS数组中，uid为1的元素（是一个对象），并把它的title改为  Lowdb
           this.mydb('db').get('RECORDS').find({ uid:1 }).assign({ title: 'Lowdb'}).write()
           // 修改成功后，可查看到db.json中的uid为1的对象的title的值为 Lowdb
        },
        delData(){
            //删除db.json里RECORDS数组中 uid为1的对象，删除的前提是uid为1的数据存在
             this.mydb('db').get('RECORDS').remove({ uid: 1 }).write()
        }
    }
}    
</script>