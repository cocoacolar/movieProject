<template>
  <!-- gallery -->
  <li v-if="movie.genres.includes(genre)||genre===0" class="col-md-6 col-lg-4 gallery tall-gallery" data-groups='["photography", "print"]'>
      <figure class="gallery-item effect-bubba">
          <img :src="movie.poster_path" alt="">
          <figcaption>
              <div class="hover-content">
                  <h2 class="hover-title text-center text-white">{{ movie.title }}</h2><!-- / hover-title -->
                  <p class="gallery-info text-center text-white">평점: {{ movie.vote_average }}
                  <p class="gallery-info text-center text-white">장르: {{ movie.genres }}
                      <span class="gallery-icons">
                          <a href="#x" @click="moveToDetail" class="gallery-button" data-toggle="modal" data-target=".print-product"><i class="fas fa-plus"></i></a>
                          <a href="shopping-cart.html" class="gallery-button"><i class="fas fa-shopping-cart"></i></a>
                      </span><!--/ gallery-icons -->
                  </p><!-- / gallery-info -->
              </div><!-- / hover-content -->
          </figcaption>
      </figure><!-- / gallery-item -->
  </li><!-- / gallery -->
</template>

<script>
export default {
  name: 'MovieListItem',
  props: {
    movie: {
      type: Object,
    },
    genre: {
      type: Number,
    }
  },
  methods: {
    moveToDetail: function () {
      this.$router.push({ name: 'MovieDetail', params: { movieId: this.movie.id } })
    }
  }
}
</script>

<style>

</style>