import Vue from 'vue'
import VueRouter from 'vue-router'
//import Home from '../views/Home.vue'
import Login from '../views/Login'
import Index from '../views/index'
import Data from '../views/Data'
import Gauge from "../views/Gauge";
import Setting from '../views/setting'

Vue.use(VueRouter);

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Index,
    children:[
      {
        path:'/setting',
        name:'Setting',
        component:Setting

      },
      {
        path:'/data',
        name:'Data',
        component: Data
      },
      {
        path:'/gauge',
        name:'Gauge',
        component:Gauge
      }
    ]
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
  path:'/login',
  name:'Login',
  component:Login
  }
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

export default router
