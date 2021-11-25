<template>
  <div>
    <div class="container">
        <header class="home-header parallax">
            <div class="header-content dark text-center">
                <h1 class="header-title mb-0">{{ userData.username }}'s Profile</h1>
            </div><!-- / header-content -->
        </header>
    </div><!-- / container -->

    <div class="spacer-2x">&nbsp;</div>

    <section id="contact-info">
        <div class="container">
            <div class="row">
                <div class="col-md-4">
                    <div class="contact-box inner-space text-center">
                        <i class="fas fa-users contact-icon mb-3"></i>
                        <h5 class="box-title">MBTI</h5>
                        <h2 class="box-description mt-4">{{ userData.mbti }}</h2>

                    </div><!-- / contact-box -->
                </div><!-- / column -->
                <div class="col-md-4">
                    <div class="contact-box inner-space text-center">
                        <i class="fas fa-thumbs-up contact-icon mb-3"></i>
                        <h5 class="box-title">LIKE</h5>
                        <h2 class="box-description mt-4">{{ articleLikeNumber }}</h2>
                    </div><!-- / contact-box -->
                </div><!-- / column -->
                <div class="col-md-4">
                    <div class="contact-box inner-space text-center">
                        <i class="fas fa-copy contact-icon mb-3"></i>
                        <h5 class="box-title">Articles</h5>
                        <h2 class="box-description mt-4">{{ userData.articles.length }}</h2>
                    </div><!-- / contact-box -->
                </div><!-- / column -->
            </div><!-- / row --> 
        </div><!-- / container -->
    </section><!-- / contact-info -->

    <div class="spacer-2x">&nbsp;</div>

    <div class="footer-widgets">
        <div class="container">
            <div class="row">
                <div class="col-lg-3 text-center">
                    <div class="widget">
                        <h3 class="widget-title">CONTACT US</h3>
                        <ul class="footer-list pl-0 mb-0">
                            <li class="mb-3"><a href="tel:01234567890"><i class="fas fa-phone mr-2"></i> 0123 456 7890</a></li>
                            <li class="mb-3"><a href="mailto:info@youriste.com"><i class="fas fa-envelope mr-2"></i> {{ userData.email }}</a></li>
                            <li class="mb-3"><a href="#x"><i class="fab fa-twitter mr-2"></i> @GallerioTwitter</a></li>
                        </ul>
                    </div><!-- / widget -->
                </div><!-- / column-->
            </div><!-- / row -->
        </div><!-- / container -->
    </div><!-- / footer-widgets -->    
  </div>
</template>

<script>
import axios from 'axios'
import { mapActions} from 'vuex'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'UserProfile.vue',
  data: function () {
    return {
      userData: {},
      articleLikeNumber: 0,
    }
  },
  props: {
    userId: {
      type: Number,
    }
  },
  methods: {
    ...mapActions(['getCurrentUser']),
    getUserProfile: function () {
      axios({
        method: 'get',
        url: `${SERVER_URL}/accounts/get-user-proflie/${this.userId}/`,
      })
        .then((res) => {
        //   console.log(res)
          this.userData = res.data
          const articles = this.userData.articles
          for (let article of articles) {
              this.articleLikeNumber += article.like_user.length
          }
        })
        .catch((err) => {
          console.log(err)
        })
    },

  },
  created: function () {
    this.getCurrentUser()
    this.getUserProfile()

    // console.log("YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    // console.log(this.userId)
    // console.log(this.userData)
    // this.setToken()
  },
}
</script>

<style>

</style>