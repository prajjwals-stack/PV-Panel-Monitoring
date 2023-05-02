import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import "bootstrap/dist/css/bootstrap.min.css"
import './axios'
createApp(App).use(router).mount('#app')
import "bootstrap/dist/js/bootstrap.js"