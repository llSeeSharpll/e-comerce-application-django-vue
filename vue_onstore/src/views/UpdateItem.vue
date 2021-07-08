<template>
  <div class="additem-page mt-6">
    <div class="columns is-multiline">
      <div class="column is-4 is-offset-4">
        <h1 class="title">Add item up for sale</h1>
        <form @submit.prevent="submitForm">
          <div class="field">
            <label>Item name</label>
            <div class="control">
              <input type="text" class="input" v-model="get_product.name" />
            </div>
          </div>
          <div class="field">
            <div class="select">
              <select v-model="get_product.get_category">
                <option disabled value="">Category</option>
                <option>Violin</option>
                <option>Viola</option>
                <option>Cello</option>
                <option>Guitar</option>
                <option>Bow</option>
              </select>
            </div>
          </div>
          <div class="field">
            <label>Description</label>
            <div class="control">
              <textarea
                type="text"
                class="input"
                v-model="get_product.description"
              />
            </div>
          </div>
          <div class="field">
            <label>Price</label>
            <div class="control">
              <input type="number" class="input" v-model="get_product.price" />
            </div>
          </div>
          <div class="notification is-danger" v-if="error.length">
            <p v-for="error in errors" :key="error">{{ error }}</p>
          </div>
          <div class="field">
            <div class="control">
              <button class="button is-dark">Update item</button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>


<script>
import axios from "axios";
import { toast } from "bulma-toast";
export default {
  name: "UpdateItem",
  data() {
    return {
      get_product: {},
      error: [],
    };
  },
  mounted() {
    this.getProduct()
    if (localStorage.getItem("username") != undefined) {
      this.username = localStorage.getItem("username");
    }
  },
  methods: {
    async getProduct() {
      this.$store.commit("setIsLoading", true);

      const category_slug = this.$route.params.category_slug;
      const product_slug = this.$route.params.product_slug;

      await axios
        .get(`/api/v1/products/${category_slug}/${product_slug}`)
        .then((response) => {
          this.get_product = response.data;
          document.title = this.product.name + " | PDVstore";
        })
        .catch((error) => {
          console.log(error);
        });
      this.$store.commit("setIsLoading", false);
    },
    async submitForm() {
      this.get_product.slug = this.get_product.name.replace(/\s/g, "-"); //HimynameisFlavio
      let formData = new FormData();
      formData.append("username", this.get_product.get_username);
      formData.append("name", this.get_product.name);
      formData.append("price", this.get_product.price);
      formData.append("description", this.get_product.description);
      formData.append("category", this.get_product.get_category);
      formData.append("slug", this.get_product.slug);
      axios.post("/api/v1/products/updateItem/", formData).then(() => {
        toast({
        message: "Update Done",
        type: "is-success",
        dismissible: true,
        pauseOnHover: true,
        duration: 2000,
        position: "bottom-right",
      });
      this.$router.push('/my-Account')
      });
    },
  },
};
</script>