import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import axios from 'axios'
import echarts from 'echarts/lib/echarts';
import locale from 'element-ui/lib/locale/lang/en'




Vue.prototype.$echarts = echarts;

Vue.use(ElementUI,{locale});
Vue.config.productionTip = false;
Vue.prototype.$axios = axios;


new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app');
