<template>
  <div class="signup-page mt-6">
    <div class="columns">
      <div class="column is-4 is-offset-4">
        <h1 class="title">Sign up</h1>
        <form @submit.prevent="submitForm">
          <div class="field">
            <label>Fistname</label>
            <div class="control">
              <input type="text" class="input" v-model="firstname" />
            </div>
          </div>
          <div class="field">
            <label>Lastname</label>
            <div class="control">
              <input type="text" class="input" v-model="lastname" />
            </div>
          </div>
          <div class="field">
            <label>Username*</label>
            <div class="control">
              <input type="text" class="input" v-model="username" />
            </div>
          </div>
          <div class="field">
            <label>Password*</label>
            <div class="control">
              <input type="password" class="input" v-model="password" />
            </div>
          </div>
          <div class="field">
            <label>Password2*</label>
            <div class="control">
              <input type="password" class="input" v-model="password2" />
            </div>
          </div>
          <div class="field">
            <label>Email*</label>
            <div class="control">
              <input type="email" class="input" v-model="email" />
            </div>
          </div>
          <div class="notification is-danger" v-if="errors.length">
            <p v-for="error in errors" :key="error">{{ error }}</p>
          </div>
          <div class="field">
            <div class="control">
              <button class="button is-dark">Sign up</button>
            </div>
          </div>
          <hr />
          Or <router-link to="/log-in">Click here to login</router-link>
        </form>
      </div>
    </div>
  </div>
</template>


<script>
import axios from "axios";
import { toast } from "bulma-toast";
export default {
  name: "SignUp",
  data() {
    return {
      username: "",
      password: "",
      password2: "",
      firstname: "",
      lastname: "",
      email: "",
      errors: [],
    };
  },
  mounted(){
      document.title = 'Sign Up | PDVstore'
  },
  methods: {
    submitForm() {
      this.errors = [];
      if (this.username === "") {
        this.errors.push("The username is missing");
      }
      if (this.password === "") {
        this.errors.push("The password too short");
      }
      if (this.password2 !== this.password) {
        this.errors.push("The password doesn't match");
      }
      if (this.email === "") {
        this.errors.push("The email is missing");
      }
      if (!this.errors.length) {
        const formData = {
          username: this.username,
          password: this.password,
          email: this.email,
          firstname: this.firstname,
          lastname: this.lastname
        };
        axios
          .post("api/v1/users/", formData)
          .then(() => {
            toast({
              message: "Account created succussfull, please login now!",
              type: "is-success",
              dismissible: true,
              pauseOnHover: true,
              duration: 2000,
              position: "bottom-right",
            });
            this.$router.push("/log-in");
          })
          .catch((error) => {
            if (error.response) {
              for (const property in error.response.data) {
                this.errors.push(
                  `${property}: ${error.response.data[property]}`
                );
              }
              console.log(JSON.stringify(error.response.data));
            } else if (error.message) {
              this.errors.push("Something went wrong. Please try again");

              console.log(JSON.stringify(error));
            }
          });
      }
    },
  },
};
</script>