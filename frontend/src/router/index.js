import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home'
import MovieDetail from '@/views/movies/MovieDetail'
import ArticleList from '@/views/articles/ArticleList'
import ArticleDetail from '@/views/articles/ArticleDetail'
import ArticleUpdate from '@/views/articles/ArticleUpdate'
import ArticleCreate from '@/views/articles/ArticleCreate'
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/movies/:movieId/',
    name: 'MovieDetail',
    component: MovieDetail,
    props: true,
  },
  {
    path: '/community/articles',
    name: 'ArticleList',
    component: ArticleList
  },
  {
    path: '/community/articles/:articleId',
    name: 'ArticleDetail',
    component: ArticleDetail,
    props: true,
  },
  {
    path: '/community/articles/:articleId/update',
    name: 'ArticleUpdate',
    component: ArticleUpdate,
    props: true,
  },
  {
    path: '/community/articles/create',
    name: 'ArticleCreate',
    component: ArticleCreate,
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup,
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
