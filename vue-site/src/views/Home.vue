<template>
  <div class="home">
    {{ info }}
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'

export default {
  name: 'Home',
  data() {
    return {
      info: []
    }
  },
  mounted() {
    axios
      .get('/idea/')
      .then(response => (this.info = response))
  }
}
</script>
