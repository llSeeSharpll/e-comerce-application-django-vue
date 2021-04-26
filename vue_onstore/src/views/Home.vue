<template>
  <div class="home mt-5">
    <section class="background-image image-fluid pb-600 ">
      <div class="hero is-medium mb-6">
        <div class="heor- has-text-centered">
          <p class="title mb-6">Welcome to PDVstore</p>
          <p class="subtitle">The best string instrument store online</p>
        </div>
      </div>
    </section>

    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">Latest products</h2>
      </div>
      <ProductBox
        v-for="product in latestProducts"
        :key="product.id"
        :product="product"
      />
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from "axios";
import ProductBox from "@/components/ProductBox";
export default {
  name: "Home",
  data() {
    return {
      latestProducts: [],
    };
  },
  components: {
    ProductBox,
  },
  mounted() {
    this.getLatestProducts();
    document.title = "Home | PDVstore";
  },
  methods: {
    async getLatestProducts() {
      this.$store.commit("setIsLoading", true);

      await axios
        .get("/api/v1/latest-products/")
        .then((respone) => {
          this.latestProducts = respone.data;
        })
        .catch((error) => {
          console.log(error);
        });
      this.$store.commit("setIsLoading", false);
    },
  },
};
</script>


<style scoped>
.background-image{
  background-image: url('../assets/images/strings-mainpage.png');
  background-size: 1270px !important;
}
.pb-600{
  
  padding-bottom: 600px;
}
</style>




