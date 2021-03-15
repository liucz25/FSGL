// import 'xe-utils'

import Vue from 'vue'
// import VXETable from 'vxe-table'
// import 'vxe-table/lib/style.css'
Vue.use(VXETable)
import App from './App.vue'


Vue.config.productionTip = false

new Vue({
    render: h => h(App),
}).$mount('#app')