<template>
  <div>
    <vxe-table
      border
      resizable
      show-overflow
      :data="tableData"
      :edit-config="{ trigger: 'click', mode: 'cell' }"
    >
      <vxe-table-column type="seq" width="60"></vxe-table-column>
      <vxe-table-column
        field="name"
        title="Name"
        :edit-render="{ name: 'input', attrs: { type: 'text' } }"
      >
      </vxe-table-column>
      <vxe-table-column
        field="nickname"
        title="Role"
        :edit-render="{ name: 'input', attrs: { type: 'text' } }"
      >
      </vxe-table-column>
      <vxe-table-column
        field="sex"
        title="Sex"
        :edit-render="{ name: '$select', options: sexList }"
      >
      </vxe-table-column>
      <vxe-table-column
        field="sex2"
        title="多选下拉"
        :edit-render="{
          name: '$select',
          options: sexList,
          props: { multiple: true },
        }"
      ></vxe-table-column>
      <vxe-table-column
        field="num1"
        title="Amount"
        :edit-render="{ name: '$input', props: { type: 'float', digits: 2 } }"
      ></vxe-table-column>
      <vxe-table-column
        field="date12"
        title="Date"
        :edit-render="{ name: '$input', props: { type: 'date' } }"
      >
      </vxe-table-column>
      <vxe-table-column
        field="date13"
        title="Week"
        :edit-render="{ name: '$input', props: { type: 'week' } }"
      >
      </vxe-table-column>
    </vxe-table>
    <el-button @click="getData">获取数据</el-button>
    <br />数据:{{ tableData }}
  </div>
</template>

<script>
export default {
  data() {
    let dta = this.mydb("vxedb").get("tableData").value();

    return { tableData:dta ,
    sexList: [{
                label: '',
                value: ''
            }, {
                label: '男',
                value: '1'
            }, {
                label: '女',
                value: '0'
            }]
    };

  },
  methods: {
    getData() {

    let dta = this.mydb("vxedb").get("tableData").value();

    return { tableData:dta };
    },

    gd() {
      alert("fdsa");
    },
  },
};
</script>