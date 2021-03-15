<template>
  <div>
    <h2>配置</h2>
    <vxe-table border resizable show-overflow :data="configData">
      <vxe-table-column field="xX" title="写平片"> </vxe-table-column>
      <vxe-table-column field="xCT" title="写CT"> </vxe-table-column>
      <vxe-table-column field="xCTC" title="写CT增强"> </vxe-table-column>
      <vxe-table-column field="xCTA" title="写CTA"> </vxe-table-column>
      <vxe-table-column field="xMR" title="写MR"> </vxe-table-column>
      <vxe-table-column field="sX" title="审平片"> </vxe-table-column>
      <vxe-table-column field="sCT" title="审CT"> </vxe-table-column>
      <vxe-table-column field="sCTC" title="审CT增强"> </vxe-table-column>
      <vxe-table-column field="sCTA" title="审CTA"> </vxe-table-column>
      <vxe-table-column field="sMR" title="审MR"> </vxe-table-column>
    </vxe-table>

    <h2>计算</h2>
    <vxe-table
      border
      resizable
      show-overflow
      :data="tableData"
      :edit-config="{ trigger: 'click', mode: 'cell' }"
    >
      <vxe-table-column type="seq" width="60"></vxe-table-column>
      <vxe-table-column field="name" title="姓名"> </vxe-table-column>
      <vxe-table-column
        field="xX"
        title="写平片"
        :edit-render="{ name: 'input', attrs: { type: 'text' } }"
      >
      </vxe-table-column>
      <vxe-table-column
        field="xCT"
        title="写CT"
        :edit-render="{ name: 'input', attrs: { type: 'text' } }"
      >
      </vxe-table-column>
      <vxe-table-column
        field="sX"
        title="审平片"
        :edit-render="{ name: 'input', attrs: { type: 'text' } }"
      >
      </vxe-table-column>
            <vxe-table-column title="写平片分值">
        <template v-slot="{ row }">
          <span>{{ countAmount(row) }} 分</span>
        </template>
      </vxe-table-column>   
         </vxe-table-column>
            <vxe-table-column title="写CT分值">
        <template v-slot="{ row }">
          <span>{{ countAmountCT(row) }} 分</span>
        </template>
      </vxe-table-column>
    </vxe-table>

    <br />数据:{{ tableData }}<br /><br />{{ configData }}

  </div>
</template>

<script>
import config from "../../public/fsgl-data.json";

export default {
  name: "lcz-Table",
  data() {
    return {
      tableData: config.config.dataGongZuoLiang,
      configData: config.config.cGongZuoLiang,
    };
  },
  methods:{
    countAmount (row) {
    //   return Number(row.xX) * Number(2)
      return Number(row.xX) * this.configData[0].xX
    },
    countAmountCT (row) {
    //   return Number(row.xX) * Number(2)
      return Number(row.xCT) * this.configData[0].xCT
    },
    countAllAmount (data) {
      let count = 0
      data.forEach(row => {
        count += this.countAmount(row)
      })
      return count
    }
    }

};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
