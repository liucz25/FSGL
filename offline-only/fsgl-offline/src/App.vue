<template>
  <div id="app">

<gzl></gzl>
<lczTable></lczTable>

  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import gzl from './components/gzl.vue'
import lcztable from './components/lcz-table.vue'
import lczTable from './components/lcz-table.vue'
export default {
  name: 'App',
  components: {
    HelloWorld,
    gzl,
    lczTable
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
