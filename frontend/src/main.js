import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'
// import './assets/css/bootstrap.min.css'
import './assets/css/style.css'
import $ from 'jquery'
// import BootstrapVue from 'bootstrap-vue'
// bootstrap
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
// fontawesome
import './assets/css/fontawesome-all.min.css'
// import 'bootstrap-vue/dist/bootstrap-vue.css'

// vue-moment
import VueMoment from 'vue-moment'

Vue.config.productionTip = false
// Vue.use(BootstrapVue)
Vue.use($)
Vue.use(VueMoment)

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
