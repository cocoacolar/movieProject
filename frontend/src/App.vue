<template>
  <div id="app">
    <!-- <div id="preloader">
        <div class="preloader">
            <span></span>
            <span></span>
        </div>
    </div> -->

    <div class="top-menu top-menu-primary">
        <div class="container">
            <p>
                <span class="social margin-fix left">
                    <a class="no-margin" href="#"><i class="fab fa-facebook-f"></i></a>
                    <a href="#"><i class="fab fa-twitter"></i></a>
                    <a href="#"><i class="fab fa-google-plus-g"></i></a>
                    <a href="#"><i class="fab fa-instagram"></i></a>
                    <a href="#"><i class="fab fa-pinterest"></i></a>
                </span>
                <span class="right">
                    <span v-if="isLogin">
                      <router-link @click.native="goToProfile" to="#"><i class="fas fa-fire mr-1"></i><span>Profile</span></router-link>
                    </span>
                    <span v-if="isLogin">
                      <router-link @click.native="logout" to="#"><i class="fas fa-user mr-1"></i><span>Logout</span></router-link>
                    </span>
                    <span v-else>
                      <a href="#x" data-toggle="modal" data-target=".login-modal"><i class="fas fa-user mr-1"></i> <span>Login</span></a>
                      <a href="#x" data-toggle="modal" data-target=".register-modal"><i class="fas fa-lock mr-1"></i> <span>Register</span></a>
                    </span>
                </span>
            </p>
        </div><!-- / container -->
    </div><!-- / top-menu -->
    <nav class="navbar navbar-expand-lg navbar-light bg-white custom-menu split-menu">
        <div class="container">
            <button class="navbar-toggler collapsed" type="button" data-toggle="collapse" data-target="#navbar-toggle-1" aria-controls="navbar-toggle-1" aria-expanded="false" aria-label="Toggle navigation">
                <span class="icon-bar top-bar"></span>
                <span class="icon-bar middle-bar"></span>
                <span class="icon-bar bottom-bar"></span>
                <span class="sr-only">Toggle navigation</span>
            </button><!-- / navbar-toggler -->

            <!-- <a class="navbar-brand mobile-brand m-auto" href="/"><img src="@/assets/images/logo-icon.png" alt=""></a> -->

            <button class="navbar-toggler collapsed" type="button" data-toggle="collapse" data-target="#navbar-toggle-2" aria-controls="navbar-toggle-2" aria-expanded="false" aria-label="Toggle navigation">
                <span class="icon-bar top-bar"></span>
                <span class="icon-bar middle-bar"></span>
                <span class="icon-bar bottom-bar"></span>
                <span class="sr-only">Toggle navigation</span>
            </button><!-- / navbar-toggler -->

            <div class="collapse navbar-collapse" id="navbar-toggle-1">
                <ul class="navbar-nav mr-auto">
                    <li class="nav-item">
                      <router-link to="/" class="nav-link">Home</router-link>
                    </li>
                    <li class="nav-item">
                      <router-link :to="{ name: 'MbtiMovieRecommend'}" class="nav-link">MBTI추천영화</router-link>
                    </li>
                </ul><!-- / navbar-nav -->
            </div><!-- / navbar-collapse -->

            <a class="navbar-brand m-auto" href="/"><img src="@/assets/images/logo-icon.png" alt=""></a>

            <div class="collapse navbar-collapse" id="navbar-toggle-2">
                <ul class="navbar-nav ml-auto">
                    <li class="nav-item">
                      <router-link :to="{ name: 'ArticleList' }" class="nav-link">Community</router-link>
                    </li>
                    <li class="nav-item">
                      <router-link to="#" class="nav-link">MyMovies</router-link>
                    </li>
                    <!-- <li class="nav-item dropdown extra-dropdowns">
                        <a class="nav-link last-menu-item has-dropdown-toggle dropdown-toggle" href="#x" id="dropdown3" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Profile<span class="count count-primary">2</span></a>
                        <div class="dropdown-menu animated fadeIn fast" aria-labelledby="dropdown3">
                            <div class="cart-small">
                                <img src="images/product-small1.jpg" alt="">
                                <p><a href="#x" class="text-black">Amazing Framed Art</a> <br> <span>1 x $29.99</span></p>
                                <a href="#x"> <i class="md-icon dp14 close-icon">close</i></a>
                            </div>
                            <div class="cart-small">
                                <img src="images/product-small2.jpg" alt="">
                                <p><a href="#x" class="text-black">Printed Photography</a> <br> <span>1 x $14.99</span></p>
                                <a href="#x"> <i class="md-icon dp14 close-icon">close</i></a>
                            </div>
                            <p class="text-left cart-small-total"><b>Subtotal: $44.98</b></p>
                            <div class="cart-small-footer text-center">
                                <div class="row">
                                    <div class="col-sm-6">
                                        <a href="shopping-cart.html" class="mini-cart-btn"><i class="md-icon dp12 mr-1">shopping_cart</i> <span class="va-middle"><b>VIEW CART</b></span></a>
                                    </div>
                                    <div class="col-sm-6">
                                        <a href="checkout.html" class="mini-cart-btn mb-0"><i class="md-icon dp12 mr-1">exit_to_app</i> <span class="va-middle"><b>CHECKOUT</b></span></a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </li>/ dropdown -->
                </ul><!-- / navbar-nav -->
            </div><!-- / navbar-collapse -->
        </div><!-- / container -->
    </nav><!-- / split-navbar -->

    <!-- modals -->

    <!-- login-modal -->
    <div class="modal fade login-modal" tabindex="-1" role="dialog">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">LOG IN</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>

                </div><!-- / modal-header -->
                <div class="modal-body">
                    <div class="custom-form">
                        <div class="form-wrapper">
                            <input type="text" class="form-control mb-3" id="login-input" placeholder="Username" v-model="credentials.username">
                            <input @keyup.enter="userLogin(credentials)" type="password" class="form-control mb-3" id="login-password-input" placeholder="Password" v-model="credentials.password">
                            <div class="form-inline-extras">
                                <div class="left-area">
                                    <!-- <div class="checkbox checkbox-primary ml-2">
                                        <label class="hidden"><input type="checkbox"></label>
                                        <input id="checkbox5" type="checkbox">
                                        <label for="checkbox5">
                                            Remember Me
                                        </label>
                                    </div>/ checkbox -->
                                </div><!-- / left-area -->
                                <div class="right-area">
                                    <a @click="userLogin(credentials)" href="#" class="btn btn-primary rectangle">LOG IN</a>
                                </div><!-- / right-area -->
                            </div><!-- / form-inline-extras -->
                            <!-- <div class="text-left mt-2">
                                <a href="#x">Forgot your password?</a>
                            </div>/ text-left -->
                        </div><!-- / form-wrapper -->
                    </div><!-- / custom-form -->
                </div><!-- / modal-body -->
            </div><!-- / modal-content -->
        </div><!-- / modal-dialog -->
    </div><!-- / modal -->
    <!-- / login-modal -->

    <!-- register-modal -->
    <div class="modal fade register-modal" tabindex="-1" role="dialog">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">REGISTER</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div><!-- / modal-header -->
                <div class="modal-body">
                    <div class="custom-form">
                        <div class="form-wrapper">
                            <input type="text" class="form-control mb-3" id="register-username" placeholder="Username" v-model="registerCredentials.username">
                            <input type="password" class="form-control mb-3" id="register-password-input" placeholder="Password" v-model="registerCredentials.password">
                            <input type="password" class="form-control mb-3" id="register-confirm-password" placeholder="Confirm Password" v-model="registerCredentials.passwordConfirmation">
                            <input type="email" class="form-control mb-3" id="register-email" placeholder="Email Address" v-model="registerCredentials.email">
                            <select id="mbti" class="custom-select" name="mbti" v-model="registerCredentials.mbti">
                              <option selected>Choose MBTI</option>
                              <option value="ISFJ">ISTJ</option>
                              <option value="ISFJ">ISFJ</option>
                              <option value="INFJ">INFJ</option>
                              <option value="INTJ">INTJ</option>
                              <option value="ISTP">ISTP</option>
                              <option value="ISFP">ISFP</option>
                              <option value="INFP">INFP</option>
                              <option value="INTP">INTP</option>
                              <option value="ESTP">ESTP</option>
                              <option value="ESFP">ESFP</option>
                              <option value="ENFP">ENFP</option>
                              <option value="ENTP">ENTP</option>
                              <option value="ESTJ">ESTJ</option>
                              <option value="ESFJ">ESFJ</option>
                              <option value="ENFJ">ENFJ</option>
                              <option value="ENTJ">ENTJ</option>
                            </select>
                            <div class="form-inline-extras sixty-fourty">
                                <div class="left-area">
                                </div><!-- / left-area -->
                                <div class="right-area">
                                    <a @click="register(registerCredentials)" href="#x" class="btn btn-primary rectangle">REGISTER</a>
                                </div><!-- / right-area -->
                            </div><!-- / form-inline-extras -->
                        </div><!-- / form-wrapper -->
                    </div><!-- / custom-form -->
                </div><!-- / modal-body -->
            </div><!-- / modal-content -->
        </div><!-- / modal-dialog -->
    </div><!-- / modal -->
    <!-- / register-modal -->

    <router-view/>
  </div>
</template>

<script>
import axios from 'axios'
import { mapState, mapActions } from 'vuex'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'App',
  data: function () {
    return {
      isLogin: false,
      credentials: {
        username: '',
        password: '',
      },
      registerCredentials: {
        username: '',
        password: '',
        passwordConfirmation: '',
        mbti: '',
        email: '',
      }
    }
  },
  methods: {   
    ...mapActions(['getCurrentUser', 'setToken']),
    logout: function () {
      localStorage.removeItem('jwt')
      this.isLogin = false
      this.$router.go()
      // this.$router.push({ name: 'Home' })
    },
    userLogin: function (credentials) {
      console.log(credentials)
      // axios
      axios.post(`${SERVER_URL}/accounts/api-token-auth/`, this.credentials)
        .then((res) => {
          // console.log(res)
          localStorage.setItem('jwt', res.data.token)
          this.isLogin = true
          // this.getCurrentUser() 
        })
        .then(() => {
          setTimeout(() => {
            console.log("자는중")
            this.getCurrentUser()
          }, 1000)
        })
        .then(() => {
          console.log("새로고침 가즈아")
          this.$router.go()
        })
        .catch((err) => {
          console.log(err)
        })
    },    
    register: function (credentials) {
      // console.log(credentials)
      // axios
      axios.post(`${SERVER_URL}/accounts/signup/`, credentials)
        .then(() => {
          // console.log(res)
          this.$router.go()
        })
        .catch((err) => {
          console.log(err)
        })
    }, 
    goToProfile : function () {
      this.setToken()
      this.getCurrentUser()
      console.log("goToProfile currentUser출력")
      console.log(this.currentUser)
      // console.log(this.currentUser)
      this.$router.push({ name: 'UserProfile', params: { userId: this.currentUser.id } })
    }
  },
  created: function () {
    // 1. Vue instance가 생성된 직후에 호출되어 jwt를 가져오기
    const token = localStorage.getItem('jwt')
    // 2. 토큰이 있다면
    if (token) {
      // 3. true로 변경하고, 없으면 유지한다.
      this.isLogin = true
    }
  },
  computed: {
    ...mapState(["currentUser"])
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>


