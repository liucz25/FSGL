<template>
<div>
 <vxe-table border resizable show-overflow :data="tableData" :edit-config="{trigger: 'click', mode: 'cell'}">
            <vxe-table-column type="seq" width="60"></vxe-table-column>
            <vxe-table-column field="name" title="Name" :edit-render="{name: 'input', attrs: {type: 'text'}}">
            </vxe-table-column>
            <vxe-table-column field="nickname" title="Role" :edit-render="{name: 'input', attrs: {type: 'text'}}">
            </vxe-table-column>
            <vxe-table-column field="sex" title="Sex" :edit-render="{name: '$select', options: sexList}">
            </vxe-table-column>
            <vxe-table-column field="sex2" title="多选下拉" :edit-render="{name: '$select', options: sexList, props: {multiple: true}}"></vxe-table-column>
            <vxe-table-column field="num1" title="Amount" :edit-render="{name: '$input', props: {type: 'float', digits: 2}}"></vxe-table-column>
            <vxe-table-column field="date12" title="Date" :edit-render="{name: '$input', props: {type: 'date'}}">
            </vxe-table-column>
            <vxe-table-column field="date13" title="Week" :edit-render="{name: '$input', props: {type: 'week'}}">
            </vxe-table-column>
        </vxe-table>

        <br>数据:{{tableData2}}
  </div>
</template>

<script>
    import config from '../../public/fsgl-data.json'

    export default {
        name: 'lcz-Table',
        data() {
            return {
                 tableData:config.config.dataGongZuoLiang,
                  tableData2: [
                { id: 10001, name: 'Test1', role: 'Develop', sex: 'Man', age: 28, address: 'vxe-table 从入门到放弃' },
                { id: 10002, name: 'Test2', role: 'Test', sex: 'Women', age: 22, address: 'Guangzhou' },
                { id: 10003, name: 'Test3', role: 'PM', sex: 'Man', age: 32, address: 'Shanghai' },
                { id: 10004, name: 'Test4', role: 'Designer', sex: 'Women ', age: 24, address: 'Shanghai' }
              ]
             }
        },


}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
