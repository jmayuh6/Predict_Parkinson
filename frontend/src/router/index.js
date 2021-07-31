import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

const routeOptions = [
  { path: '/', name: 'Home' },
  { path: '/audio', name: 'Audio' }
]

const routes = routeOptions.map(r => {
  return {
    ...r,
    component: () => import(`@/views/${r.name}/Index.vue`)
  }
})

const router = new Router({
  routes,
  mode: 'history'
})

export default router
