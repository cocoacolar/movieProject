<template>
  <div>
    <h1>Update 페이지 입니다.</h1>
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
    <button @click="updateArticle">수정</button>
    <button @click="deleteArticle">삭제</button>
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
    ...mapActions(['loadArticle', 'setToken']),
    updateArticle: function () {
      axios({
        method: 'put',
        url: `${SERVER_URL}/community/${this.articleId}/delete-update/`,
        data: this.articleData,
        headers: this.config
      })
        .then((res) => {
          console.log(res)
          this.$router.push({ name: 'ArticleDetail', params: { articleId: this.article.id } })
        })
        .catch((err) => {
          console.log(err)
        })
    },
    loadArticle: function () {
      this.articleData.title = this.article.title
      this.articleData.movie_title = this.article.movie_title
      this.articleData.content = this.article.content
      this.articleData.mbti = this.article.mbti
    },
    deleteArticle: function () {
      axios({
        method: 'delete',
        url: `${SERVER_URL}/community/${this.articleId}/delete-update/`,
        headers: this.config
      })
        .then((res) => {
          console.log(res)
          this.$router.push({ name: 'ArticleList' })
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  created: function () {
    this.loadArticle(this.articleId)
    this.setToken()
    // console.log(this.config)
    console.log(this.article)
  },
  props: {
    articleId: {
      type: Number,
    }
  },
  computed: {
    ...mapState(["article", "config"])
  }
}
</script>

<style>

</style>