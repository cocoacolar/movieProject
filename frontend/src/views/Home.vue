<template>
  <div>
    <h1>MovieList</h1>
    <MovieListItem v-for="(movie, index) in movieList" :key="index" :movie="movie"/>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
import MovieListItem from '@/components/MovieListItem'

export default {
  name: 'Home',
  components: {
    MovieListItem,
  },
  methods: {
    ...mapActions(["loadMovieList"]),
  },
  created: function () {
    this.loadMovieList()
  },
  computed: {
    ...mapState(["movieList"])
  }
}
</script>

<style>

</style>