<template>
  <div>
    <div class="card d-inline-block" style="width: 18rem;">
      <img :src="movie.poster_path" class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">{{ movie.title }}</h5>
        <a href="#" class="btn btn-primary" @click="moveToDetail">Go somewhere</a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieListItem',
  props: {
    movie: {
      type: Object,
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