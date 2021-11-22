<template>
  <div>
    <h1>ArticleList</h1>
    <button @click="createArticle">게시글 쓰기</button>
    <ArticleListItem v-for="(article, index) in articleList" :key="index" :article="article"/>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
import ArticleListItem from '@/components/ArticleListItem'

export default {
  name: 'ArticleList',
  components: {
    ArticleListItem,
  },
  methods: {
    ...mapActions(["loadArticleList"]),
    createArticle: function () {
      this.$router.push({ name: 'ArticleCreate'})
    }
  },
  created: function () {
    this.loadArticleList()
  },
  computed: {
    ...mapState(["articleList"])
  }
}
</script>

<style>

</style>