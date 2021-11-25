<template>
  <div>
    <div class="container">
        <header class="article-header parallax" >
            <div class="header-content dark text-center">
                <h1 class="header-title mb-0">게시판</h1>
            </div><!-- / header-content -->
        </header>
    </div><!-- / container -->  

    <div class="spacer-2x">&nbsp;</div>

    <section id="posts">
        <div class="container">
            <div class="row">
                <div class="col-md-8 blog-content">
                    <ArticleListItem v-for="(article, index) in articleList" :key="index" :article="article"/>
                    <nav aria-label="pagination-center">
                        <button @click="createArticle" class="btn btn-primary">게시글 쓰기</button>
                        <ul class="pagination justify-content-center">
                            <li class="page-item active"><a class="page-link" href="#x">1</a></li>
                            <li class="page-item"><a class="page-link" href="#x">2</a></li>
                            <li class="page-item"><a class="page-link" href="#x">3</a></li>
                            <li class="page-item disabled"><a class="page-link" href="#x">...</a></li>
                            <li class="page-item"><a class="page-link" href="#x">9</a></li>
                            <li class="page-item"><a class="page-link" href="#x"><i class="fas fa-long-arrow-alt-right"></i></a></li>
                        </ul>
                    </nav><!-- / pagination -->
                </div><!-- / blog-content -->

                <div class="col-md-4 blog-sidebar mt-3">
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