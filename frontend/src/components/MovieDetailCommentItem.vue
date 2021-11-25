<template>
  <li class="media">
    <div class="media-left">
        <a href="#x">
            <img class="media-object" alt="" src="images/creator.jpg">
        </a>
    </div>
    <div class="media-body">
        <div class="comment-info">
            <div class="comment-date text-sm"><i class="far fa-clock mr-1"></i> {{ comment.updated_at }} <button @click="deleteComment" class="btn btn-danger">x</button></div>
            <div class="comment-author"><a href="#x"><b>{{ comment.user.username }}</b></a></div>
        </div><!-- / comment-info -->
        <div class="comment">
            <p class="mb-0">{{ comment.content }}</p>
        </div><!-- / comment -->
        <div>
          <p class="mb-0">평점: {{ comment.rank }}</p>
        </div>
        <!-- <a href="#" @click="deleteComment" class="gallery-button" data-toggle="modal" data-target=".print-product"><i class="fas fa-plus"></i></a> -->
        <!-- <button @click="deleteComment" class="btn btn-danger">삭제</button> -->
        <hr>        
    </div><!-- / parent media-body -->
  </li><!-- / media -->
</template>

<script>
import { mapState, mapActions } from 'vuex'
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'MovieDetailCommentItem',
  props: {
    comment: {
      type: Object,
    },
    movieId: {
      type: Number,
    },
  },
  methods: {
    ...mapActions(['setToken']),
    deleteComment: function () {
      this.setToken()
      axios({
        method: 'delete',
        url: `${SERVER_URL}/movies/comments/${this.comment.id}/delete/`,
        headers: this.config
      })
        .then((res) => {
          console.log(res)
          // this.$router.push({ name: 'MovieDetail', params: { movieId: this.movieId } }).catch(()=>{})
          this.$router.go()
        })
        .catch((err) => {
          console.log(err)
        })
    },
  }, 
  computed: {
    ...mapState(["config"])
  }
}
</script>

<style>

</style>

