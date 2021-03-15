# [vue 动态合并单元格、并添加小计合计功能](https://www.cnblogs.com/shuihanxiao/p/11081192.html)

 

1、效果图

![img](https://img2018.cnblogs.com/blog/1079233/201906/1079233-20190625095553129-68340346.png)

2、后台返回数据格式（平铺式）

 

![img](https://img2018.cnblogs.com/blog/1079233/201906/1079233-20190625095834122-1149075556.png)

 

3、后台返回数据后，整理所需要展示的属性存储到（items）数组内

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
  var obj = {
              "id": curItems[i].id,
              "feeName": curItems[i].feeName,
              "projectName": curItems[i].projectName,
              "projectDetailsName": curItems[i].projectDetailsName,
              "zbMoney": curItems[i].zbMoney,
              "qyMoney": curItems[i].qyMoney,
              "projectId": curItems[i].projectId,
              "instructions": curItems[i].instructions,
              "contentText": curItems[i].contentText,
              "measureText": curItems[i].measureText
            }
            if (curItems[i].projectDetailsName == '合计:') {
              obj.projectName = curItems[i - 1].projectName
            }
            _self.items.push(obj)
          }
        
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

4、调用initData(调用后会删除需要合并的字段内容)

 _self.initData()

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
 initData(){
        const that = this;
        let arry = [];
        let itemsCopy = JSON.parse(JSON.stringify(that.items));
        for (let i = 0; i < itemsCopy.length; i++) {
          for (let j = (i + 1); j < itemsCopy.length; j++) {
            for (let h in itemsCopy[i]) {
              for (let k in itemsCopy[j]) {
                if (k == 'feeName' || k == 'projectName' || k == 'projectDetailsName') {
                  if (itemsCopy[j][k] != '小计:' && itemsCopy[j][k] != '合计:') {
                    if (h === k && itemsCopy[i][h] === itemsCopy[j][k]) {
                      delete  itemsCopy[j][k]
                    }
                  }
                }
              }
            }
          }
          arry.push(itemsCopy[i]);
        }
        that.dataT = arry;
      },
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

 

![img](https://img2018.cnblogs.com/blog/1079233/201906/1079233-20190625100601118-408050435.png)

 

4、合并行数的代码

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
 rowSpanF: function (key, val) {
        const that = this;
        let num = 0;
        for (let i in that.items) {
          for (let j in that.items[i]) {
            if (j == 'feeName' || j == 'projectName' || j == 'projectDetailsName') {
              if (key === j && val === that.items[i][j]) {
                if (that.items[i][j] == '小计:' || that.items[i][j] == '合计:') {
                  return
                }
                num++;
              }
            }
          }
        }

        if(num==0){
            return 1
        }
        return num;
      },
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

5、html

![img](https://img2018.cnblogs.com/blog/1079233/201906/1079233-20190625100906601-1572452118.png)

代码如下：

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
<tr v-for="(item,$index) in dataT">　　   　　　　
          <td
            v-if="key!='id'&&(key=='feeName'||key=='projectName'||key=='projectDetailsName'||key=='zbMoney'||key=='qyMoney'||key=='projectId'||key=='instructions'||key=='contentText'||key=='measureText')"
            v-for="(val,key) in item" :rowspan="rowSpanF(key,val)">
            <span v-if="key=='feeName'">{{val}}</span>
            <span v-if="key=='projectName'">{{val}}</span>
            <span v-if="key=='projectDetailsName'">{{val}}</span>
            <span v-if="key=='zbMoney'">{{val}}</span>
            <span v-if="key=='qyMoney'">{{val}}</span>
            <span v-if="key=='projectId'">{{item['zbMoney']+item['qyMoney']}}</span>
            <span v-if="key=='instructions'">{{val}} </span>
            <span v-if="key=='contentText'">{{val}}</span>
            <span v-if="key=='measureText'">{{val}}</span>
          </td>
          <td>
            <div v-if="item.projectDetailsName!='小计:'&&item.projectDetailsName!='合计:'">
              <!--<span @click="toAdd(allItems[$index])"><a>添加</a></span>-->
              <span @click="toEdit(item)"><a>编辑</a></span>
              <span>
                  <a-popconfirm
                    title="确定删除吗?"
                    okText="确定"
                    cancelText="取消"
                    @confirm="() => deletArr(item)">
                       <a href="javascript:;">删除</a>
                  </a-popconfirm>
              </span>
            </div>
          </td>　　　　
        </tr>
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

 注意事项：
后台返回数据必须符合该条件

![img](https://img2018.cnblogs.com/blog/1079233/201906/1079233-20190625101841741-982533989.png)

 

![img](https://img2018.cnblogs.com/blog/1079233/201906/1079233-20190625102018107-472223987.png)