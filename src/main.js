import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import 'jquery'
import 'popper.js'
import 'bootstrap'
import VueResource from 'vue-resource'
import image2base64 from 'image-to-base64'
Vue.use(VueResource)
Vue.config.productionTip = false
Object.defineProperty(Vue.prototype, '$image2base64', { value: image2base64 });

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
