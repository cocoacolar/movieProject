<template>
  <div>
    <div class="container">
        <header class="home-header parallax" >
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
                        <div class="about-widget">
                            <h4 class="widget-title text-center">ABOUT ME</h4>
                            <div class="about-image text-center">
                                <img src="images/creator.jpg" alt="">
                            </div><!-- / about-image -->
                            <p class="text-center">Quisque tincidunt sodales ante, nec porttitor sem pharetra vitae. Nullam quis dui sit amet lectus facilisis iaculis pulvinar.</p>
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