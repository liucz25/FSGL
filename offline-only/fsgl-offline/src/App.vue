<template>
  <div id="app">
<!-- 
<gzl></gzl>
<lczTable></lczTable> -->
<vtable></vtable>

  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import gzl from './components/gzl.vue'
import lczTable from './components/lcz-table.vue'
import vtable from './components/vtable.vue'

export default {
  name: 'App',
  components: {
    HelloWorld,
    gzl,
    lczTable,
    vtable
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
