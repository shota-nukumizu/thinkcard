<template>
  <h1>Index Page</h1>
  <div class="home" v-for="item in info" v-bind:key="item.id">
    {{ item.title }}
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'

export default {
  name: 'Home',
  data() {
    return {
      info: {}
    }
  },
  mounted() {
    axios
      .get('/idea/')
      .then(response => (this.info = response.data))
  }
}
</script>
