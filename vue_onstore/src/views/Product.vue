<template>
  <div class="page-product mt-6">
    <div class="columns is-multiline">
      <div class="column is-8">
        <div
          id="carouselExampleIndicators"
          class="carousel slide"
          data-ride="carousel"
        >
          <div class="carousel-inner">
            <div
              v-for="(image, imageIndex) in product.get_image"
              :key="image"
              class="carousel-item"
              v-bind:class="{ active: isActive == imageIndex }"
            >
              <img class="d-block w-100" :src="image" alt="First slide" />
            </div>
          </div>
          <a
            class="carousel-control-prev"
            role="button"
            @click="prev"
            data-slide="prev"
          >
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="sr-only">Previous</span>
          </a>
          <a
            class="carousel-control-next"
            role="button"
            @click="next"
            data-slide="next"
          >
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="sr-only">Next</span>
          </a>
        </div>
      </div>

      <div class="column is-4 is-size-2">
        <h1 class="title">{{ product.name }}</h1>
        <h3 class="is-size-4">Seller: {{ product.get_username }}</h3>
        <p>{{ product.description }}</p>
        <p><strong>Price: </strong>{{ product.price }}</p>
        <div
          v-if="username !== product.get_username || username == undefined"
          class="field has-addons mt-6"
        >
          <div class="control">
            <input type="number" class="input" min="1" v-model="quantity" />
          </div>
          <div class="control">
            <a class="button is-dark" @click="addToCart">Add to cart</a>
          </div>
        </div>
        <div
          v-if="username === product.get_username"
          class="field has-addons mt-6"
        >
          <div class="control mx-2">
            <router-link
              :to="{ name: 'UpdateItem'}"
              class="button is-success"
              >Update Item</router-link
            >
          </div>
          <div class="control">
            <a class="button is-danger" @click="deleteItem">Delete Item</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import axios from "axios";
import { toast } from "bulma-toast";
export default {
  name: "Product",
  data() {
    return {
      product: {},
      quantity: 1,
      username: "",
      isActive: 0,
      isUpdate: true,
    };
  },
  async mounted() {
    await this.getProduct();
    this.imageChange();
    this.$nextTick(function () {
      window.setInterval(() => {
        this.imageChange();
      }, 5000);
    });
    if (localStorage.getItem("username")) {
      this.username = localStorage.getItem("username");
    }
  },

  methods: {
    imageChange() {
      this.isActive += 1;
      if (this.isActive >= this.product.get_image.length) {
        this.isActive = 0;
      }
    },
    prev() {
      if (this.isActive === 0) {
        this.isActive = this.product.get_image.length;
      }
      this.isActive -= 1;
    },
    next() {
      if (this.isActive === this.product.get_image.length - 1) {
        this.isActive = 0;
      } else {
        this.isActive += 1;
      }
    },
    async deleteItem() {
      this.$store.commit("setIsLoading", true);

      await axios
        .post("api/v1/products/deleteItem", { username: this.username })
        .then(() => {
          console.log("done");
        })
        .catch((error) => {
          console.log(error);
        });

      this.$store.commit("setIsLoading", false);
    },
    async getProduct() {
      this.$store.commit("setIsLoading", true);

      const category_slug = this.$route.params.category_slug;
      const product_slug = this.$route.params.product_slug;

      await axios
        .get(`/api/v1/products/${category_slug}/${product_slug}`)
        .then((response) => {
          this.product = response.data;
          document.title = this.product.name + " | PDVstore";
        })
        .catch((error) => {
          console.log(error);
        });
      this.$store.commit("setIsLoading", false);
    },
    addToCart() {
      if (isNaN(this.quantity) || this.quantity < 1) {
        this.quantity = 1;
      }

      const item = {
        product: this.product,
        quantity: this.quantity,
      };

      this.$store.commit("addToCart", item);

      toast({
        message: "The product was added into the cart",
        type: "is-success",
        dismissible: true,
        pauseOnHover: true,
        duration: 2000,
        position: "bottom-right",
      });
    },
  },
  coumputed: {},
};
</script>


