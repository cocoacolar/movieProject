<template>
  <!-- gallery -->
    <li v-if="isSameMbti || mbti==='ALL'" class="col-md-6 col-lg-4 gallery tall-gallery" data-groups='["photography", "print"]'>
      <div>
        <figure class="gallery-item effect-bubba">
            <img :src="movie.poster_path" alt="">
            <figcaption>
                <div class="hover-content">
                    <h2 class="hover-title text-center text-white">{{ movie.title }}</h2><!-- / hover-title -->
                    <p class="gallery-info text-center text-white">평점: {{ movie.vote_average }}
                    <p class="gallery-info text-center text-white">장르: {{ movie.genres }}
                        <span class="gallery-icons">
                            <a href="#x" @click="moveToDetail" class="gallery-button" data-toggle="modal" data-target=".print-product"><i class="fas fa-plus"></i></a>                  
                        </span><!--/ gallery-icons -->
                    </p><!-- / gallery-info -->
                </div><!-- / hover-content -->
            </figcaption>
        </figure><!-- / gallery-item -->
      </div>
    </li><!-- / gallery -->
</template>

<script>
export default {
  name: 'MbtiMovieRecommendItem',
  data: function () {
    return {
      isSameMbti: false,
    }
  },
  props: {
    movie: {
      type: Object,
    },
    mbti: {
      type: String,
    }
  },
  methods: {
    moveToDetail: function () {
      this.$router.push({ name: 'MovieDetail', params: { movieId: this.movie.id } })
    },
    checkMbti: function () {
      const comments = this.movie.comments
      for (let comment of comments) {
        if (comment.user.mbti === this.mbti) {
          return true
        }
      }
      return false
    }
  },
  watch: {
    mbti: function () {
      this.isSameMbti = this.checkMbti()
    }
  }
}
</script>

<style>

</style>