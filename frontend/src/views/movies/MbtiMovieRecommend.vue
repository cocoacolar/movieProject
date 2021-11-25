<template>
  <div>
    <div class="container">
        <header class="mbti-header parallax">
            <div class="header-content dark text-center">
                <h1 class="header-title mb-0">MBTI 추천영화</h1>
            </div><!-- / header-content -->
        </header>
    </div><!-- / container -->

    <div class="spacer-2x">&nbsp;</div>

    <section id="gallery" class="p-0 line-effect">
        <div class="container">
            <!-- gallery filter -->
            <!-- <input type="text" id="mbti" v-model="credentials.mbti" @keypress.enter="signup(credentials)"> -->
            <select id="mbti" name="mbti" class="custom-select text-center" @change="onChange($event)">
              <option value="ALL">ALL</option>
              <option value="ISTJ">ISTJ</option>
              <option value="ISFJ">ISFJ</option>
              <option value="INFJ">INFJ</option>
              <option value="INTJ">INTJ</option>
              <option value="ISTP">ISTP</option>
              <option value="ISFP">ISFP</option>
              <option value="INFP">INFP</option>
              <option value="INTP">INTP</option>
              <option value="ESTP">ESTP</option>
              <option value="ESFP">ESFP</option>
              <option value="ENFP">ENFP</option>
              <option value="ENTP">ENTP</option>
              <option value="ESTJ">ESTJ</option>
              <option value="ESFJ">ESFJ</option>
              <option value="ENFJ">ENFJ</option>
              <option value="ENTJ">ENTJ</option>
            </select>
            <!-- / gallery filter -->
        </div><!-- / container -->
        <div class="spacer-1x">&nbsp;</div>
        <div class="container full-width">
            <!-- <h3 class="section-title hidden">GALLERY</h3> -->
            <ul class="row gallery line-effect list-unstyled mb-0" id="grid">
              <MbtiMovieRecommendItem v-for="(movie, index) in movieList" :key="index" :movie="movie" :mbti="mbti"/>
            </ul><!-- / gallery -->
        </div><!-- / container -->
    </section>
    <!-- / gallery -->

    <div class="spacer-2x">&nbsp;</div>
 
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
import MbtiMovieRecommendItem from '@/components/MbtiMovieRecommendItem'

export default {
  name: 'MbtiMovieRecommend',
  data: function () {
    return {
      mbti: 'ALL',
    }
  },
  components: {
    MbtiMovieRecommendItem,
  },
  methods: {
    ...mapActions(["loadMovieList"]),

    onChange: function (event) {
      const mbtiValue = event.target.value
      this.mbti = mbtiValue
      // console.log(this.mbti)
    },
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