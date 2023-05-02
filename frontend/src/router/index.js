import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Forecast from '../views/Forecast.vue'
import Info from '../views/Info.vue'
import biddingView from '../views/biddingView.vue'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'

const routes = [
  {
    path: '/home',
    name: 'home',
    component: HomeView
  },
  {
    path: '/Forecast',
    name: 'Forecast',
    component: Forecast
  },
  {
    path: '/Info',
    name: 'Info',
    component: Info
  },
  {
    path: '/bidding',
    name: 'biddingView',
    component: biddingView
  },
  {
    path: '/',
    name: 'LoginView',
    component: LoginView
  },
  {
    path: '/register',
    name: 'RegisterView',
    component: RegisterView
  }
  
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
