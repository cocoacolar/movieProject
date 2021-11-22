<template>
  <div>
    <h1>Detail 페이지 입니다.</h1>
    <h2>{{ article.title }}</h2>
    <p>{{ article.content }}</p>
    <p>{{ article }}</p>
    <button @click="updateArticle">수정</button>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'ArticleDetail',
  methods: {
    ...mapActions(['loadArticle', 'setToken']),
    updateArticle: function () {
      // console.log(this.config)
      axios({
        method: 'put',
        url: `${SERVER_URL}/community/${this.articleId}/delete-update/`,
        data: this.article,
        headers: this.config
      })
        .then((res) => {
          console.log(res)
          this.$router.push({ name: 'ArticleUpdate', params: { articleId: this.articleId } })
        })
        .catch((err) => {
          console.log(err)
        })
    },
    deleteArticle: function () {

    }
  },
  created: function () {
    this.loadArticle(this.articleId)
    this.setToken()
    // console.log(this.config)
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