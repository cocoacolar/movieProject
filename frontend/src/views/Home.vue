<template>
  <div>
    <div class="container">
        <header class="home-header parallax">
            <div class="header-content dark text-center">
                <h1 class="header-title mb-0">GGANG GGANG </h1>
                <p class="inner-space mb-0">MOVIE VILLAGE</p>
            </div><!-- / header-content -->
        </header>
    </div><!-- / container -->

    <section id="gallery" class="p-0 line-effect">
        <div class="container">
            <!-- gallery filter -->
            <ul class="gallery-filter list-inline text-center">
                <li><a @click.prevent="changeGenre(0)" href="#" data-group="all" class="active ml-2">ALL</a></li>
                <li><a @click.prevent="changeGenre(28)" href="#">ACTION</a></li>
                <li><a @click.prevent="changeGenre(10749)" href="#">ROMANCE</a></li>
                <li><a @click.prevent="changeGenre(35)" href="#">COMEDY</a></li>
                <li><a @click.prevent="changeGenre(878)" href="#">SF</a></li>
            </ul>
            <!-- / gallery filter -->
        </div><!-- / container -->
        <div class="container full-width">
            <!-- <h3 class="section-title hidden">GALLERY</h3> -->
            <ul class="row gallery line-effect list-unstyled mb-0" id="grid">
              <MovieListItem v-for="(movie, index) in movieList" :key="index" :movie="movie" :genre="genre"/>
            </ul><!-- / gallery -->
        </div><!-- / container -->
    </section>
    <!-- / gallery -->

    <div class="spacer-2x">&nbsp;</div>
 
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'

import MovieListItem from '@/components/MovieListItem'

export default {
  name: 'Home',
  data: function () {
    return {
      genre: 0,
    }
  },
  components: {
    MovieListItem,
  },
  methods: {
    ...mapActions(["loadMovieList", "loadGenreList"]),
    changeGenre: function (genreChoice) {
      this.genre = genreChoice
    },
  },
  created: function () {
    this.loadMovieList()
    this.loadGenreList()
  },
  computed: {
    ...mapState(["movieList", "genreList"])
  }
}


</script>


<style>

</style>