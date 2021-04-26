<template>
  <div class="Myaccount-page mt-6">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">My Account</h1>
      </div>

      <div class="column is-12">
        <router-link to="/add-item" class="button is-primary"
          >Add item</router-link
        >
      </div>

      <div class="column is-12">
        <h2 class="subtitle">My Orders</h2>
      </div>
      <div v-if="orders === []">No items ordered yet!</div>
      <OrderSummary
        v-else
        v-for="order in orders"
        :key="order.id"
        :order="order"
      />
      <div class="column is-12">
        <h2 class="subtitle">My items</h2>
      </div>
      <div v-if="products == undefined" class="column is-12">
        No items up for sale yet!
      </div>
      <ProductBox
        v-else
        class="colmn is-3"
        v-for="product in products"
        :key="product.id"
        :product="product"
      />
    </div>
  </div>
</template>


<script>
import axios from "axios";
import OrderSummary from "@/components/OrderSummary.vue";
import ProductBox from "@/components/ProductBox.vue";
export default {
  name: "MyAccount",
  mounted() {
    document.title = "My Acount | PDVstore";
    this.getMyOrders();
  },
  components: {
    OrderSummary,
    ProductBox,
  },
  data() {
    return {
      orders: [],
      products: [],
    };
  },
  methods: {
    async getMyOrders() {
      this.$store.commit("setIsLoading", true);

      await axios
        .get("/api/v1/orders/")
        .then((response) => {
          this.orders = response.data;
        })
        .catch((error) => {
          console.log(error);
        });

      await axios
        .get("/api/v1/products/")
        .then((response) => {
          this.products = response.data;
        })
        .catch((error) => {
          console.log(error);
        });

      this.$store.commit("setIsLoading", false);
    },
  },
};
</script>