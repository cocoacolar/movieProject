<template>
  <div>
    <h1>Movie Detail 페이지</h1>
    <img :src="movie.poster_path" class="card-img-top" alt="...">
    <h2>{{ movie.title }}</h2>
    <p>{{ movie.overview }}</p>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
// import axios from 'axios'

// const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'ArticleDetail',
  methods: {
    ...mapActions(['loadMovie', 'setToken']),
  },
  created: function () {
    this.loadMovie(this.movieId)
    this.setToken()
    console.log(this.config)
  },
  props: {
    movieId: {
      type: Number,
    }
  },
  computed: {
    ...mapState(["movie", "config"])
  }
}
</script>

<style>

</style>