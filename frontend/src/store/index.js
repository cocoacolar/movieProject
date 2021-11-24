import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'


const SERVER_URL = process.env.VUE_APP_SERVER_URL

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    article: {},
    articleList: [],
    movie: {},
    movieList: [],
    config: {},
    genreList: [],
    currentUser: {},
  },
  mutations: {
    LOAD_ARTICLE: function (state, result) {
      state.article = result
    },
    LOAD_ARTICLE_LIST: function (state, results) {
      state.articleList = results
    },
    LOAD_MOVIE: function (state, result) {
      state.movie = result
    },
    LOAD_MOVIE_LIST: function (state, results) {
      state.movieList = results
    },
    SET_TOKEN: function (state, config) {
      state.config = config
    },
    LOAD_GENRE_LIST: function (state, results) {
      state.genreList = results
    },
    GET_CURRENT_USER: function (state, result) {
      // console.log(typeof(result))
      state.currentUser = result
      // console.log(state.currentUser)
    }
    
  },
  actions: {
    loadArticle: function ({commit}, articleId) {
      axios({
        method: 'get',
        url: `${SERVER_URL}/community/${articleId}`
      })
        .then((res) => {
          // console.log(res)
          commit('LOAD_ARTICLE', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    loadArticleList: function ({commit}) {
      axios({
        method: 'get',
        url: `${SERVER_URL}/community/`
      })
        .then((res) => {
          // console.log(res)
          // console.log(res.data)
          commit('LOAD_ARTICLE_LIST', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    loadMovie: function ({commit}, movieId) {
      axios({
        method: 'get',
        url: `${SERVER_URL}/movies/${movieId}`
      })
        .then((res) => {
          // console.log(res)
          commit('LOAD_MOVIE', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    loadMovieList: function ({commit}) {
      axios({
        method: 'get',
        url: `${SERVER_URL}/movies/`
      })
        .then((res) => {
          // console.log(res)
          // console.log(res.data)
          commit('LOAD_MOVIE_LIST', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    loadGenreList: function ({commit}) {
      axios({
        method: 'get',
        url: `${SERVER_URL}/movies/genres/`
      })
        .then((res) => {
          commit('LOAD_GENRE_LIST', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    setToken: function () {
      const token = localStorage.getItem("jwt")
      const config = {
        Authorization: `JWT ${token}`
      }
      this.commit('SET_TOKEN', config)
    },
    getCurrentUser: function ({commit}) {
      axios({
        method: 'get',
        url: `${SERVER_URL}/accounts/get-user/`,
        headers: this.state.config
      })
        .then((res) => {
          commit('GET_CURRENT_USER', res.data)
        })
        .catch((err) => {
          console.log(err)
        })      
    }
  },  
  modules: {
  }
})
