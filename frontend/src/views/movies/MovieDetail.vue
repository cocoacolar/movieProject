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
                            <h2 href="">평점: {{ movie.vote_average }}</h2>
                            <!-- <a href="#x" class="btn-social btn-facebook m-1 rectangle"><i class="fab fa-facebook-f"></i> <span>Share - 93.3K</span></a>
                            <a href="#x" class="btn-social btn-twitter m-1 rectangle"><i class="fab fa-twitter"></i> <span>Tweet - 17.5K</span></a> -->
                            <!-- <a href="#x" class="btn-social btn-google m-1 rectangle"><i class="fab fa-google-plus-g"></i> <span>Share - 7.9K</span></a>
                            <a href="#x" class="btn-social btn-pinterest m-1 rectangle"><i class="fab fa-pinterest"></i> <span>Pin It - 7.7K</span></a> -->
                            <!-- <a href="#x" class="btn-social btn-pinterest m-1 rectangle"><i class="fab fa-pinterest"></i> <span>좋아요</span></a> -->
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
                                            <i class="far fa-star"></i>                                                
                                            <label for="mbti">RANK</label>
                                            <!-- <i class="fas fa-star-half-alt"></i> -->
                                            <i class="fas fa-star"></i>
                                            <!-- <input type="text" id="mbti" v-model="credentials.mbti" @keypress.enter="signup(credentials)"> -->
                                            <select id="mbti" name="mbti" class="custom-select" v-model="commentData.rank">
                                                <option value="1">★(1)</option>
                                                <option value="2">★★(2)</option>
                                                <option value="3">★★★(3)</option>
                                                <option value="4">★★★★(4)</option>
                                                <option value="5">★★★★★(5)</option>
                                                <option value="6">★★★★★★(6)</option>
                                                <option value="7">★★★★★★★(7)</option>
                                                <option value="8">★★★★★★★★(8)</option>
                                                <option value="9">★★★★★★★★★(9)</option>
                                                <option value="10">★★★★★★★★★★(10)</option>
                                            </select>
                                            </div>
                                        </div>
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
                      <h5 class="widget-title text-center text-primary">AD</h5>
                      <div class="about-widget">
                          <img src="https://img.asiatoday.co.kr/file/2021y/04m/14d/2021041401001299300078891.jpg" alt="">
                      </div><!-- / about-widget -->
                    </div><!-- / sidebar-widget -->

                    <div class="sidebar-widget">
                      <h5 class="widget-title text-center text-primary">AD</h5>
                      <div class="about-widget">
                          <img src="https://lh3.googleusercontent.com/proxy/b7qrXlRRi7FTMjbxggpXDRlaa3I7BQ3uW6Jn7N2mgWdRD9M7YPSxrQNlEJFdubjw3mzKcFKuYbEexpIqRh3UxtUfKRGn8VT_-1DMPDZdqez3Hu1BgFcMx_V5Csiye7_blnU2h7po89Nyk9TSywkvpg" alt="">
                      </div><!-- / about-widget -->
                    </div><!-- / sidebar-widget -->

                    <div class="sidebar-widget">
                        <h4 class="widget-title text-center pb-3">Search</h4>
                        <p class="text-center">Find the movie you want!</p>
                        <div class="input-group mt-3">
                            <input type="text" class="form-control border-faded" placeholder="Search Movie">
                            <span class="input-group-btn">
                                <a href="#x" class="btn btn-w-icon btn-primary ml-2"><span><i class="fas fa-search"></i></span></a>
                            </span>
                        </div><!-- / input-group -->
                    </div><!-- / sidebar-widget -->

                    <div class="sidebar-widget">
                        <h4 class="widget-title text-center pb-2">Supporters</h4>
                        <div class="tag-cloud">
                            <a href="https://www.ssafy.com/" class="btn btn-sm btn-black rectangle mt-1">#SSAFY</a>
                            <a href="https://hphk.kr/" class="btn btn-sm btn-black rectangle mt-1">#HPHK</a>
                            <a href="http://www.norangtongdak.co.kr/" class="btn btn-sm btn-black rectangle mt-1">#노랑통닭</a>
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
          this.$router.go()
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