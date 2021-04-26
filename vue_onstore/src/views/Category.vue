<template>
  <div class="page-category mt-6">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">
          {{ category.name }}
        </h2>
      </div>
      <ProductBox
        v-for="product in category.products"
        :key="product.id"
        :product="product"
      />
    </div>
  </div>
</template>



<script>
import axios from "axios";
import { toast } from "bulma-toast";
import ProductBox from "@/components/ProductBox";
export default {
  name: "Category",
  data() {
    return {
      category: {
        products: [],
      },
    };
  },
  components: {
    ProductBox,
  },
  mounted() {
    this.getCategory();
  },
  watch: {
    $route(to) {
      if (to.name === "Category") {
        this.getCategory();
      }
    },
  },
  methods: {
    async getCategory() {
      this.$store.commit("setIsLoading", true);

      const category_slug = this.$route.params.category_slug;

      axios
        .get(`/api/v1/products/${category_slug}/`)
        .then((response) => {
          this.category = response.data;
          document.title = this.category.name + " | PDVstore";
        })
        .catch((error) => {
          console.log(error);
          toast({
            message: "Something went wrong, please try again later",
            type: "is-danger",
            dismissible: true,
            pauseOnHover: true,
            duration: 2000,
            position: "bottom-right",
          });
        });

      this.$store.commit("setIsLoading", false);
    },
  },
};
</script>