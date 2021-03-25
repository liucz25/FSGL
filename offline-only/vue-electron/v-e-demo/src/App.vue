<template>
  <div id="app">
    <LowdbTest></LowdbTest>
    <!-- <vex-test></vex-test> -->
    <vext></vext>
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import LowdbTest from './components/LowdbTest'
import Vext from './components/vext.vue'
// import vexTest from './components/vexTest'


export default {
  name: 'App',
  components: {
    // HelloWorld
    LowdbTest,
    // vexTest,
    Vext

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
