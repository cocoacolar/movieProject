<template>
  <div>
    <div class="container">
        <header class="home-header parallax" >
            <div class="header-content dark text-center">
                <h1 class="header-title mb-0">게시글 상세</h1>
                <p class="inner-space mb-0">{{ currentUser }}</p>
                <p class="inner-space mb-0">{{ config }}</p>
            </div><!-- / header-content -->
        </header>
    </div><!-- / container -->  

    <div class="spacer-2x">&nbsp;</div>
    <section id="posts">
        <div class="container">
            <div class="row">
                <div class="col-md-8 blog-content">
                        <div class="blog block">
                            <div class="post-content">
                                <h4>제목- {{article.title}}</h4>
                                <h4>영화제목- {{ article.movie_title }}</h4>
                                <!-- <blockquote class="blockquote">
                                    <p class="mb-0">{{ movie.overview }}</p>
                                </blockquote> -->
                            </div><!-- / post-content -->
                        </div><!-- / blog-block -->

                        <div class="blog block">
                            <div class="post-content">
                                <h4>내용</h4>                        
                                <br>
                                <p class="mb-3">{{ article.content }}</p>
                                <!-- <blockquote class="blockquote">
                                    <p class="mb-0">{{ movie.overview }}</p>
                                </blockquote> -->
                            </div><!-- / post-content -->
                        </div><!-- / blog-block -->

                        <div class="spacer">&nbsp;</div>

                        <div id="share-post" class="text-center bg-white">
                            <a href="">좋야요 수:{{ article.like_user.length }}</a>
                            <!-- <a href="#x" class="btn-social btn-facebook m-1 rectangle"><i class="fab fa-facebook-f"></i> <span>Share - 93.3K</span></a>
                            <a href="#x" class="btn-social btn-twitter m-1 rectangle"><i class="fab fa-twitter"></i> <span>Tweet - 17.5K</span></a> -->
                            <!-- <a href="#x" class="btn-social btn-google m-1 rectangle"><i class="fab fa-google-plus-g"></i> <span>Share - 7.9K</span></a>
                            <a href="#x" class="btn-social btn-pinterest m-1 rectangle"><i class="fab fa-pinterest"></i> <span>Pin It - 7.7K</span></a> -->
                            <a href="#x" class="btn-social btn-pinterest m-1 rectangle"><i class="fab fa-pinterest"></i> <span>좋아요</span></a>
                        </div><!-- share-post -->

                        <div class="spacer">&nbsp;</div>
                        <div id="comments" class="comments">
                            <div class="container">
                                <h4 class="mb-3">COMMENTS ({{ article.comments.length }})</h4>

                                <div class="spacer">&nbsp;</div>

                                <ul class="media-list">
                                  <ArticleDetailCommentItem v-for="(comment, index) in article.comments" :key="index" :comment="comment" :articleId="articleId"/>
                                </ul><!-- / media-list -->

                                <div class="spacer-2x">&nbsp;</div>

                                <!-- comment form -->
                                <div id="comment-form">
                                    <h4 class="mb-3">LEAVE A COMMENT</h4>
                                    <form id="commentForm">
                                        <div class="row">
                            
                                            <div class="col-md-12">
                                                <div class="form-group">
                                                    <textarea v-model="commentData.content" id="message" class="form-control border-faded" rows="5" placeholder="*Comment"></textarea>
                                                </div>
                                            </div><!-- / sub-column -->
                                        </div><!-- / row -->

                                        <div class="text-center">
                                            <button @click="createComment" type="submit" id="form-submit" class="btn btn-primary comment-btn"><span>POST COMMENT</span></button>
                                            <div id="msgSubmit" class="h3 text-center hidden"></div>
                                            <div class="clearfix"></div> 
                                        </div><!-- / text-center -->
                                    </form><!-- / commentForm -->
                                </div>
                                <!-- / comment form -->
                            </div><!-- / container -->
                        </div><!-- / comments -->
                    </div><!-- / blog-content -->

                <div class="col-md-4 blog-sidebar mt-3">
                    <div class="sidebar-widget">
                        <div class="about-widget">
                          <button @click="updateArticle" class="btn btn-primary">수정</button>
                        </div><!-- / about-widget -->
                    </div><!-- / sidebar-widget -->

                    <div class="sidebar-widget">
                        <h4 class="widget-title text-center">RECENT POSTS</h4>
                        <div class="spacer">&nbsp;</div>
                        <div class="post-widget">
                            <ul class="list-unstyled">
                                <li>
                                    <div class="recent-posts first">
                                        <div class="recent-post-image">
                                            <img src="images/blog-post.jpg" alt="">
                                        </div><!-- / recent-post-image -->
                                        <div class="recent-post-content">
                                            <a href="single-post.html" class="recent-post-title">TRAVELING</a>
                                            <p class="text-sm mb-2">Travel</p>
                                            <p class="text-sm opc-75"><i class="far fa-clock"></i> 01 SEP 2018</p>
                                        </div><!-- / recent-post-content -->
                                    </div><!-- / recent-posts -->
                                </li>
                                <li>
                                    <div class="recent-posts pt-2">
                                        <div class="recent-post-image">
                                            <img src="images/blog-post2.jpg" alt="">
                                        </div><!-- / recent-post-image -->
                                        <div class="recent-post-content">
                                            <a href="single-post.html" class="recent-post-title">PHOTOSHOOT</a>
                                            <p class="text-sm mb-2">Photography</p>
                                            <p class="text-sm opc-75"><i class="far fa-clock"></i> 31 AUG 2018</p>
                                        </div><!-- / recent-post-content -->
                                    </div><!-- / recent-posts -->
                                </li>
                            </ul>
                        </div><!-- / post-widget -->
                    </div><!-- / sidebar-widget -->

                    <div class="sidebar-widget">
                        <h4 class="widget-title text-center pb-3">NEWSLETTER</h4>
                        <p class="text-center">Subscribe to our newsletter to get notified about new posts, informations and updates.</p>
                        <div class="input-group mt-3">
                            <input type="text" class="form-control border-faded" placeholder="Email Address">
                            <span class="input-group-btn">
                                <a href="#x" class="btn btn-w-icon btn-primary ml-2"><span><i class="fas fa-paper-plane"></i></span></a>
                            </span>
                        </div><!-- / input-group -->
                    </div><!-- / sidebar-widget -->

                    <div class="sidebar-widget">
                        <h4 class="widget-title text-center pb-2">TAGS</h4>
                        <div class="tag-cloud">
                            <a href="#x" class="btn btn-sm btn-black rectangle mt-1">#design</a>
                            <a href="#x" class="btn btn-sm btn-black rectangle mt-1">#photography</a>
                            <a href="#x" class="btn btn-sm btn-black rectangle mt-1">#videography</a>
                            <a href="#x" class="btn btn-sm btn-black rectangle mt-1">#paintings</a>
                            <a href="#x" class="btn btn-sm btn-black rectangle mt-1">#photo</a>
                            <a href="#x" class="btn btn-sm btn-black rectangle mt-1">#art</a>
                            <a href="#x" class="btn btn-sm btn-black rectangle mt-1">#travel</a>
                        </div><!-- / tag-cloud -->
                        <!-- / tags-widget -->
                    </div><!-- / sidebar-widget -->
                </div><!-- / blog-sidebar -->
            </div><!-- / row -->
        </div><!-- / container -->
    </section><!-- / posts -->  

    
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
import axios from 'axios'
import ArticleDetailCommentItem from '@/components/ArticleDetailCommentItem.vue'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'ArticleDetail',
  data: function () {
    return {
      commentData: {
        content: '',
        article_id: 0,
      }
    }
  },
  components: {
      ArticleDetailCommentItem,
  },
  methods: {
    ...mapActions(['loadArticle', 'setToken', 'getCurrentUser']),
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
    createComment: function () {
      // console.log(this.movie.id)
      this.commentData.article_id = this.articleId
      axios({
        method: 'post',
        url: `${SERVER_URL}/community/comments/create/`,
        data: this.commentData,
        headers: this.config
      })
        .then((res) => {
          console.log(res)
          // this.$router.push({ name: 'ArticleDetail', params: { articleId: res.data.id } })
          // this.$router.push({ name: 'ArticleList' })
          this.$router.go()
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  created: function () {
    this.loadArticle(this.articleId)
    this.setToken()
    this.getCurrentUser()
    // console.log(this.config)
  },
  props: {
    articleId: {
      type: Number,
    }
  },
  computed: {
    ...mapState(["article", "config", "currentUser"])
  }
}
</script>

<style>

</style>