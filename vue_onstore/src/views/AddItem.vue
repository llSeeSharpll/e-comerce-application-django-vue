<template>
  <div class="additem-page mt-6">
    <div class="columns is-multiline">
      <div class="column is-4 is-offset-4">
        <h1 class="title">Add item up for sale</h1>
        <form @submit.prevent="submitForm">
          <div class="field">
            <label>Item name</label>
            <div class="control">
              <input type="text" class="input" v-model="name" />
            </div>
          </div>
          <div class="field">
            <div class="select">
              <select v-model="category">
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
              <textarea type="text" class="input" v-model="description" />
            </div>
          </div>
          <div class="field">
            <label>Price</label>
            <div class="control">
              <input type="number" class="input" v-model="price" />
            </div>
          </div>
          <div class="field">
            <label>Image</label>
            <div class="control">
              <input type="file" multiple="multiple" class="input" @change="selectFile($event)" />
            </div>
          </div>
          <div class="notification is-danger" v-if="errors.length">
            <p v-for="error in errors" :key="error">{{ error }}</p>
          </div>
          <div class="field">
            <div class="control">
              <button class="button is-dark">Add item</button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>


<script>
import axios from "axios";
export default {
  name: "AddItem",
  data() {
    return {
      username: "",
      name: "",
      price: "",
      description: "",
      category: "",
      slug: "",
      errors: [],
      file: [],
    };
  },
  mounted() {
    if (localStorage.getItem("username") != undefined) {
      this.username = localStorage.getItem("username");
    }
  },
  methods: {
    async submitForm() {
      this.slug = this.name.replace(/\s/g, "-"); //HimynameisFlavio
      let formData = new FormData();
      for (let i = 0; i < this.file.length; i++) {
        formData.append("image"+i, this.file[i]);
      }
      formData.append("username", this.username);
      formData.append("name", this.name);
      formData.append("price", this.price);
      formData.append("description", this.description);
      formData.append("category", this.category);
      formData.append("slug", this.slug);
      let config = {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      };
      axios.post("/api/v1/products/add/", formData, config).then(() => {
        console.log("done");
      });
    },
    selectFile(event) {
      this.file = event.target.files;
      console.log(this.file);
    },
  },
};
</script>