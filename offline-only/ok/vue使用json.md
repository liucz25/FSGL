vue使用json最简单的两种方式
第一种：
首先我项目是在 webpack 下搭建的vue项目
在public文件夹下创建jsonTest.json
json 格式的数据如下：
{
	“innerList”: [
		{"attr1":"内部数据1","attr2":"内部数据2",...},
		{"attr1":"内部数据1","attr2":"内部数据2",...},
		....
	]
}
在某一组件内：

......html元素
import people from '../../json/jsonTest.json';
 
export default{
	data(){
		return {
			dataset: people.innerList
		}
	}
}

第二种：
getDataList(){
 this.$axios.get("/json/jsonTest.json").then((res)=>{
 //得到response.data数据做具体赋值操作
 }).catch(() => {
		response.errer
                    this.$message({
                        message: response.errer.msg
                    })
                })
 
分类: Vue框架