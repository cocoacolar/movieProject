<template>
  <div>
    <h1>게시글 작성 페이지 입니다.</h1>
    <div>
      <label for="title">게시글 제목:</label>
      <input type="text" id="title" v-model="articleData.title">
    </div>
    <div>
      <label for="movie_title">영화 제목:</label>
      <input type="text" id="movie_title" v-model="articleData.movie_title">
    </div>
    <div>
      <label for="content">내용:</label>
      <textarea id="content" rows="10" cols="33" v-model="articleData.content"></textarea>
    </div>
    <div>
      <label for="mbti">MBTI:</label>
      <select id="mbti" name="mbti" v-model="articleData.mbti">
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
    </div>
    <button @click="createArticle">작성</button>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'ArticleUpdate',
  data: function () {
    return {
      articleData: {
        title: '',
        movie_title: '',
        content: '',
        mbti: '',
      }
    }
  },
  methods: {
    ...mapActions(['setToken']),
    createArticle: function () {
      axios({
        method: 'post',
        url: `${SERVER_URL}/community/`,
        data: this.articleData,
        headers: this.config
      })
        .then((res) => {
          console.log(res)
          this.$router.push({ name: 'ArticleDetail', params: { articleId: res.data.id } })
          // this.$router.push({ name: 'ArticleList' })
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  created: function () {
    this.setToken()
  },
  computed: {
    ...mapState(["config"])
  }
}
</script>

<style>

</style>