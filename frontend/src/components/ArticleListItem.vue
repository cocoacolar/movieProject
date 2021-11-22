<template>
  <div>
    <span @click="moveToDetail">{{ article.title }}</span>
  </div>
</template>

<script>
export default {
  name: 'ArticleListItem',
  props: {
    article: {
      type: Object,
    }
  },
  methods: {
    moveToDetail: function () {
      // this.$router.push({ name: 'ArticleDetail', params: { articleId: this.article.id, article: this.article} })]
      // console.log(typeof(this.article.id))
      this.$router.push({ name: 'ArticleDetail', params: { articleId: this.article.id } })
    }
  }
}
</script>

<style>

</style>