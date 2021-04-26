import { createStore } from 'vuex'

export default createStore({
  state: {
    cart: {
      items: [],
    },
    isAuthenticated: false,
    token: '',
    isLoading: false,
    username: ''
  },
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem("cart")) {
        let tempcart = JSON.parse(localStorage.getItem('cart'))
        //state.cart = tempcart
        for (let i = 0; i < tempcart.items.length; i++) {
          if (tempcart.items[i].product.get_username === localStorage.getItem('username')) {
            state.cart.items.push(tempcart.items[i])
          }
        }
      }
      else {
        localStorage.setItem('cart', JSON.stringify(state.cart))
      }

      if (localStorage.getItem('token')) {
        state.token = localStorage.getItem('token')
        state.isAuthenticated = true
      }
      else {
        state.token = ''
        state.isAuthenticated = false
      }
    },
    addToCart(state, item) {
      const exists = state.cart.items.filter(i => i.product.id === item.product.id)
      if (exists.length) {
        exists[0].quantity = parseInt(exists[0].quantity) + parseInt(item.quantity)
      } else {
        state.cart.items.push(item)
      }

      localStorage.setItem('cart', JSON.stringify(state.cart))
    },
    setIsLoading(state, status) {
      state.isLoading = status
    },
    setToken(state, token) {
      state.token = token
      state.isAuthenticated = true
    },
    setUsername(state, username) {
      state.username = username
    },
    removeToken(state) {
      state.token = ''
      state.isAuthenticated = false
    },
    removeUsername(state) {
      state.username = ''
    },
    resetCart(state){
      state.cart = { item: [] }
    },
    clearCart(state) {
      state.cart = { item: [] }

      localStorage.setItem('cart', JSON.stringify(state.cart))
    }
  },
  actions: {
  },
  modules: {
  }
})
