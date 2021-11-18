<template>
  <div>
    <h1>Signup</h1>
    <div>
      <label for="username">사용자 이름:</label>
      <input type="text" id="username" v-model="credentials.username">
    </div>
    <div>
      <label for="password">비밀번호:</label>
      <input type="password" id="password" v-model="credentials.password">
    </div>
    <div>
      <label for="passwordConfirmation">비번 확인:</label>
      <input type="password" id="passwordConfirmation" v-model="credentials.passwordConfirmation" @keypress.enter="signup(credentials)">
    </div>
    <div>
      <label for="mbti">MBTI:</label>
      <input type="text" id="mbti" v-model="credentials.mbti" @keypress.enter="signup(credentials)">
    </div>
    <div>
      <label for="email">이메일:</label>
      <input type="text" id="email" v-model="credentials.email" @keypress.enter="signup(credentials)">
    </div>
    <button @click="signup(credentials)">회원가입</button>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Signup',
  data: function () {
    return {
      credentials: {
        username: '',
        password: '',
        passwordConfirmation: '',
        mbti: '',
        email: '',
      }
    }
  },
  methods: {
    signup: function (credentials) {
      // console.log(credentials)
      // axios
      axios.post(`${SERVER_URL}/accounts/signup/`, credentials)
        .then(() => {
          // console.log(res)
          this.$router.push({ name: 'Login' })
        })
        .catch((err) => {
          console.log(err)
        })
    }
  }
}
</script>