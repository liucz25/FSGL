import Vue from 'vue'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import App from './App.vue'


import db from './utils/datastore.js'


Vue.use(ElementUI);
Vue.use(db)

Vue.config.productionTip = false
    // Vue.config.productionTip = true
new Vue({
    render: h => h(App),
}).$mount('#app')