vxe-table 可编辑-数据联动计算
http://jsrun.net/JQWKp/edit

html



```html
<script src="https://cdn.jsdelivr.net/npm/vue"></script>
<script src="https://cdn.jsdelivr.net/npm/xe-utils"></script>
<script src="https://cdn.jsdelivr.net/npm//vxe-table"></script>
<!-- 使用 cdn 引用方式需要注意是否锁定版本，默认指向最新版本 -->

<div id="app">
  <template>
    <div>
      <vxe-table
      border
      resizable
      show-footer
      :data="tableData"
      :footer-method="footerMethod"
      :edit-config="{trigger: 'click', mode: 'cell'}">
      <vxe-table-column type="seq" width="60"></vxe-table-column>
      <vxe-table-column field="name" title="书名" :edit-render="{name: 'input'}"></vxe-table-column>
      <vxe-table-column field="amount" title="单价" :edit-render="{name: 'input', attrs: {type: 'number'}}"></vxe-table-column>
      <vxe-table-column field="number" title="数量" :edit-render="{name: 'input', attrs: {type: 'number'}}"></vxe-table-column>
      <vxe-table-column title="总价">
        <template v-slot="{ row }">
          <span>{{ countAmount(row) }} 元</span>
        </template>
      </vxe-table-column>
    </vxe-table>
    </div>
  </template>
</div>
```



js

```javascript
var Main = {
  data() {
    return {
      tableData: [
        { name: 'vxe-table 从入门到放弃', amount: 80, number: 5 },
        { name: 'JavaScript 权威指南', amount: 40, number: 3 },
        { name: 'Vue 入门到精通', amount: 90, number: 9 },
        { name: '深入现代 JavaScript 应用开发', amount: 60, number: 1 }
      ]
    }
  },
  methods: {
    countAmount (row) {
      return Number(row.amount) * Number(row.number)
    },
    countAllAmount (data) {
      let count = 0
      data.forEach(row => {
        count += this.countAmount(row)
      })
      return count
    },
    handleSum(list, field){
      var total = 0
      for(var index=0;index<list.length;index++){
        total += Number(list[index][field] || 0)
      }
      return total
    },
    footerMethod ({ columns, data }) {
      return [
        columns.map((column, columnIndex) => {
          if (columnIndex === 0) {
            return '合计'
          }
          if (columnIndex === 3) {
            return `${this.handleSum(data, 'number')} 本`
          } else if (columnIndex === 4) {
            return `共 ${this.countAllAmount(data)} 元`
          }
          return '-'
        })
      ]
    }
  }
};
var Ctor = Vue.extend(Main);
new Ctor().$mount('#app')


```

1
vxe-table 从入门到放弃
80
5
400 元
2
JavaScript 权威指南
40
3
120 元
3
Vue 入门到精通
90
9
810 元
4
深入现代 JavaScript 应用开发
60
1
60 元
合计
-
-
18 本
共 1390 元