<template>
  <div>
  <div>
    <div class="container">
        <header class="home-header parallax" >
            <div class="header-content dark text-center">
                <h1 class="header-title mb-0">게시글수정</h1>
            </div><!-- / header-content -->
        </header>
    </div><!-- / container -->  

    <div class="spacer-2x">&nbsp;</div>

    <div class="modal-body">
      <div class="custom-form">
        <div class="form-wrapper">
          <input type="text" class="form-control mb-3" placeholder="게시글 제목" id="title" v-model="articleData.title">
          <input type="text" class="form-control mb-3" placeholder="영화 제목" id="movei_title" v-model="articleData.movie_title">
          <textarea id="content" class="form-control mb-3" placeholder="내용" rows="10" cols="33" v-model="articleData.content"></textarea>
          <select class="custom-select" id="mbti" name="mbti" v-model="articleData.mbti">
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
      </div>
    </div>
    <button @click="updateArticle" class="btn btn-primary">수정</button>
    <button @click="deleteArticle" class="btn btn-primary">삭제</button>
    <div class="spacer-2x">&nbsp;</div>
    <div class="spacer-2x">&nbsp;</div>
  </div>
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