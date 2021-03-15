<template>
  <div class="gzl">
      <h2>helloworld</h2>
    {{fenconfig}}
  </div>
</template>

<script>
    import config from '../../public/fsgl-data.json'

    export default {
         name: 'gzl',
        data() {
            return {
                 fenconfig:config.config.dataGongZuoLiang
             }
        },


}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
