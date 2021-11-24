<template>
  <div>
    <div class="container">
        <header class="home-header parallax" >
            <div class="header-content dark text-center">
                <h1 class="header-title mb-0">{{ movie.title }}</h1>
                <p class="inner-space mb-0">{{ movie.release_date }}</p>
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
                                <h4>줄거리</h4>
                                <br>
                                <p class="mb-3">{{ movie.overview }}</p>
                                <!-- <blockquote class="blockquote">
                                    <p class="mb-0">{{ movie.overview }}</p>
                                </blockquote> -->
                            </div><!-- / post-content -->
                        </div><!-- / blog-block -->

                        <div class="spacer">&nbsp;</div>

                        <div id="share-post" class="text-center bg-white">
                            <a href="">평점:{{ movie.vote_average }}</a>
                            <!-- <a href="#x" class="btn-social btn-facebook m-1 rectangle"><i class="fab fa-facebook-f"></i> <span>Share - 93.3K</span></a>
                            <a href="#x" class="btn-social btn-twitter m-1 rectangle"><i class="fab fa-twitter"></i> <span>Tweet - 17.5K</span></a> -->
                            <!-- <a href="#x" class="btn-social btn-google m-1 rectangle"><i class="fab fa-google-plus-g"></i> <span>Share - 7.9K</span></a>
                            <a href="#x" class="btn-social btn-pinterest m-1 rectangle"><i class="fab fa-pinterest"></i> <span>Pin It - 7.7K</span></a> -->
                            <a href="#x" class="btn-social btn-pinterest m-1 rectangle"><i class="fab fa-pinterest"></i> <span>좋아요</span></a>
                        </div><!-- share-post -->

                        <div class="spacer">&nbsp;</div>

                        <div id="comments" class="comments">
                            <div class="container">
                                <h4 class="mb-3">COMMENTS ({{ movie.comments.length }})</h4>

                                <div class="spacer">&nbsp;</div>

                                <ul class="media-list">
                                  <MovieDetailCommentItem v-for="(comment, index) in movie.comments" :key="index" :comment="comment" :movieId="movieId"/>
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
                            <img :src="movie.poster_path" alt="">
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
import MovieDetailCommentItem from '@/components/MovieDetailCommentItem'
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'MovieDetail',
  data: function () {
    return {
      commentData: {
        content: '',
        movie_id: 0,
        rank: 5,
      }
    }
  },
  methods: {
    ...mapActions(['loadMovie', 'setToken']),
    createComment: function () {
      // console.log(this.movie.id)
      this.commentData.movie_id = this.movieId
      axios({
        method: 'post',
        url: `${SERVER_URL}/movies/comments/create/`,
        data: this.commentData,
        headers: this.config
      })
        .then((res) => {
          console.log(res)
          // this.$router.push({ name: 'ArticleDetail', params: { articleId: res.data.id } })
          // this.$router.push({ name: 'ArticleList' })
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  components: {
    MovieDetailCommentItem,
  },
  created: function () {
    this.loadMovie(this.movieId)
    this.setToken()
    // console.log(this.config)
  },
  props: {
    movieId: {
      type: Number,
    }
  },
  computed: {
    ...mapState(["movie", "config"])
  }
}
</script>

<style>
</style>