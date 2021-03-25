import DataStore from 'lowdb'
import FileSync from 'lowdb/adapters/FileSync'
import path from 'path'

export default {
    install(Vue) { // 该行固定写法，安装vue.js插件时，关于install方法，参考vue官网，https://cn.vuejs.org/v2/api/
        Vue.prototype.mydb = function(FileName) { //  将 mydb 这个方法挂载在Vue的原型上,FileName是json文件的名字
            const NamePath = path.join('./public', `/json/${FileName}.json`) // 拿到传入的json的存储路径;该json文件存在public文件夹下的json文件夹下。
            const adpets = new FileSync(NamePath) // 初始化lowdb读写的json文件名以及存储路径
            const data = DataStore(adpets) // lowdb接管该文件
            return data
        }
    }
}