<template>
  <div id="app">
<h2>helloworld</h2>
<gzl></gzl>

  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import gzl from './components/gzl.vue'

export default {
  name: 'App',
  components: {
    HelloWorld,
    gzl
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
