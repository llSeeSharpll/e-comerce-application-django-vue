<template>
  <div class="wrapper">
    <nav class="navbar is-dark is-fixed-top">
      <div class="navbar-brand d-flex justify-content-between">
        <router-link to="/" class="navbar-item">PDVstore</router-link>
        <a
          class="navbar-burger ml-auto"
          aria-label="menu"
          aria-expanded="false"
          data-target="navbar-menu"
          @click="mobileshow()"
        >
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>
      <div
        v-if="show"
        class="navbar-menu"
        id="navbar-menu"
        v-bind:class="{ 'is-active': showMobileMenu }"
      >
        <div class="navbar-start">
          <div class="navbar-item">
            <form method="get" action="/search">
              <div class="field has-addons">
                <div class="control">
                  <input
                    type="text"
                    class="input"
                    placeholder="What you looking for?"
                    name="query"
                  />
                </div>
                <div class="control">
                  <button @click="toggleNavbar()" class="button is-success">
                    <span class="icon"><i class="fas fa-search"></i></span>
                  </button>
                </div>
              </div>
            </form>
          </div>
        </div>
        <div class="navbar-end">
          <router-link @click="toggleNavbar()" to="/bow" class="navbar-item"
            >Bow</router-link
          >
          <router-link @click="toggleNavbar()" to="/violin" class="navbar-item"
            >Violin</router-link
          >
          <router-link @click="toggleNavbar()" to="/viola" class="navbar-item"
            >Viola</router-link
          >
          <router-link @click="toggleNavbar()" to="/cello" class="navbar-item"
            >Cello</router-link
          >
          <router-link
            @click="toggleNavbar()"
            to="/double-bass"
            class="navbar-item"
            >Double Bass</router-link
          >
          <router-link @click="toggleNavbar()" to="/guitar" class="navbar-item"
            >Guitar</router-link
          >
          <div class="navbar-item">
            <div class="buttons">
              <template v-if="$store.state.isAuthenticated">
                <router-link to="/my-Account" class="button is-light"
                  >{{ username }}'s Account</router-link
                >
                <button @click="logout()" class="button is-danger">
                  Log out
                </button>
              </template>
              <template v-else>
                <router-link
                  @click="toggleNavbar()"
                  to="/log-in"
                  class="button is-light"
                  >Log in</router-link
                >
                <router-link
                  @click="toggleNavbar()"
                  to="/sign-up"
                  class="button is-light"
                  >Sign Up</router-link
                >
              </template>
              <router-link
                @click="toggleNavbar()"
                to="/cart"
                class="button is-success"
              >
                <span class="icon"><i class="fas fa-shopping-cart"></i></span>
                <span>Cart ({{ cartTotalLength }})</span>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </nav>
    <div
      class="is-loading-bar has-text-centered"
      v-bind:class="{ 'is-loading': $store.state.isLoading }"
    >
      <div class="lds-dual-ring"></div>
    </div>
    <section class="section">
      <router-view />
    </section>
    <footer class="footer">
      <p class="has-text-centered">Copyright (c) 2021</p>
    </footer>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      showMobileMenu: false,
      cart: {
        items: [],
      },
      username: "",
      show: true,
    };
  },
  mounted() {
    this.show = true;
    this.cart = this.$store.state.cart;
    if (localStorage.getItem("username")) {
      this.username = localStorage.getItem("username");
    }
  },
  beforeCreate() {
    this.$store.commit("initializeStore");
    const token = this.$store.state.token;

    if (token) {
      axios.defaults.headers.common["Authorization"] = "Token " + token;
    } else {
      axios.defaults.headers.common["Authorization"] = "";
    }
  },
  methods: {
    mobileshow() {
      if (this.show == false) {
        this.toggleNavbar();
      }
      this.showMobileMenu = !this.showMobileMenu;
    },
    toggleNavbar() {
      this.show = !this.show;
    },
    logout() {
      this.toggleNavbar();
      axios.defaults.headers.common["Authorization"] = "";
      localStorage.removeItem("token");
      localStorage.removeItem("username"), localStorage.removeItem("userid");
      this.$store.commit("removeToken");
      this.$store.commit("removeUsername");
      this.$store.commit("resetCart");
      this.$router.push("/");
    },
  },
  computed: {
    cartTotalLength() {
      let totalLength = 0;
      if (this.$store.state.isAuthenticated) {
        for (let i = 0; i < this.cart.items.length; i++) {
          totalLength += this.cart.items[i].quantity;
        }
      }

      return totalLength;
    },
  },
};
</script>

<style lang="scss">
@import "../node_modules/bulma";

.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
}
.lds-dual-ring:after {
  content: " ";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #ccc;
  border-color: #ccc transparent #ccc transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}
@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
.is-loading-bar {
  height: 0;
  overflow: hidden;
  -webkit-transition: all 0.3s;
  transition: all 0.3s;
  &.is-loading {
    height: 80px;
  }
}
</style>
