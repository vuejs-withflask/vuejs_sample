import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
// import test from '@/components/test'
// import users from '@/components/users'
import home from '@/components/home'
import list_users from '@/components/list_users'
import registration from '@/components/registration'
import login from '@/components/login';
import logged from '@/components/logged';


Vue.use(Router)

export default new Router({
  routes: [
    {
      path:'/home',
      name:'home',
      component:home
    },
    {
      path:'/',
      name:'hello world',
      component:HelloWorld
    },
    {
      path:'/listusers',
      name:'listusers',
      component:list_users
    },
    {
      path:'/registration',
      name:"registration",
      component:registration
    },
    {
      path:'/login',
      name:"login",
      component:login
    },
    {
      path:'/logged',
      component:logged,
    }
  ]
})
