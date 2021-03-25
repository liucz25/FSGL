import Vue from 'vue'
import db from './utils/datastore.js'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import VXETable from 'vxe-table'
import 'vxe-table/lib/style.css'


import App from './App.vue'



Vue.use(db)
Vue.use(ElementUI);
Vue.use(VXETable)


Vue.config.productionTip = false
    // Vue.config.productionTip = true
new Vue({
    render: h => h(App),
}).$mount('#app')