
<template>
  <div>
<h1>不显示数据，未找到原因</h1>

    <vxe-table ref="xTable" :data.sync="tableData">
      <!-- <vxe-table-column type="index" label="Number" width="80"></vxe-table-column> -->
      <vxe-table-column prop="name" label="Name"></vxe-table-column>
      <vxe-table-column prop="sex" label="Sex"></vxe-table-column>
      <vxe-table-column prop="address" label="Address"></vxe-table-column>
    </vxe-table>
  </div>
</template>

<script>
export default {
  data () {
    return {
      tableData: [
        {
          id: 10001,
          name: 'test1',
          role: 'developer',
          sex: 'Man',
          address: 'address abc123'
        }
      ]
    }
  }
}
</script>