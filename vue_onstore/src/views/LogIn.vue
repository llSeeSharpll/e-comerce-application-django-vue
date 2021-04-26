<template>
  <div class="login-page mt-6">
    <div class="columns">
      <div class="column is-4 is-offset-4">
        <h1 class="title">Sign up</h1>
        <form @submit.prevent="submitForm">
          <div class="field">
            <label>Username</label>
            <div class="control">
              <input type="text" class="input" v-model="username" />
            </div>
          </div>
          <div class="field">
            <label>Password</label>
            <div class="control">
              <input type="password" class="input" v-model="password" />
            </div>
          </div>
          <div class="notification is-danger" v-if="errors.length">
            <p v-for="error in errors" :key="error">{{ error }}</p>
          </div>
          <div class="field">
            <div class="control">
              <button class="button is-dark">Log in</button>
            </div>
          </div>
          <hr />
          Or <router-link to="/sign-up">Click here to Signup</router-link>
        </form>
      </div>
    </div>
  </div>
</template>


<script>
import axios from "axios";
export default {
  name: "LogIn",
  data() {
    return {
      username: "",
      password: "",
      errors: [],
    };
  },
  mounted() {
    document.title = "Log In | PDVstore";
  },
  methods: {
    async submitForm() {
      axios.defaults.headers.common["Authorization"] = "";
      localStorage.removeItem("token");
      const formData = {
        username: this.username,
        password: this.password,
      };
      await axios
        .post("/api/v1/token/login/", formData)
        .then((response) => {
          const token = response.data.auth_token;
          this.$store.commit("setToken", token);
          this.$store.commit("setUsername",this.username)
          localStorage.setItem("username",this.username)

          axios.defaults.headers.common["Authorization"] = "Token " + token;
          localStorage.setItem("token", token);
          window.location.href='http://localhost:8080/my-Account'
        })
        .catch((error) => {
          if (error.response) {
            for (const property in error.response.data) {
              this.errors.push(`${property}: ${error.response.data[property]}`);
            }
          } else {
            this.errors.push("Something went wrong. Please try again");

            console.log(JSON.stringify(error));
          }
        });
    },
  },
};
</script>