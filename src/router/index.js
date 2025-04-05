// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import Page from '../components/index.vue';
import Login from '../components/login.vue';
import choose_your_puppy from '../components/choose_your_puppy.vue';
import before_started from '../components/before_started.vue';
import running from '../components/running.vue';
import nearby from '../components/nearby.vue';
import shop from '../components/shop.vue';
import vip from '../components/vip.vue';
import running_home from '../components/running_home.vue';
import home from '../components/home.vue';
import running_details from '../components/running_details.vue';

const routes = [
  {
    path: '/',
    name: 'Page',
    component: Page
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/choose_your_puppy',
    name: 'choose_your_puppy',
    component: choose_your_puppy
  },
  {
    path: '/before_started',
    name: 'before_started',
    component: before_started
  },
    {
    path: '/running_home',
    name: 'running_home',
    component: running_home
  },
  {
    path: '/running',
    name: 'running',
    component: running
  },
  {
    path: '/running_details',
    name: 'running_details',    
    component: running_details
  },
  {
    path: '/home',
    name: 'home',     
    component: home
  },

  {
    path: '/nearby',
    name: 'nearby',
    component: nearby
  },
  {
    path: '/shop',  
    name: 'shop',
    component: shop
  },
  {
    path: '/vip',
    name: 'vip',
    component: vip
  },

];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
