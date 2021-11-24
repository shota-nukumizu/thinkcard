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
      .get('http://127.0.0.1:8000/idea/')
      .then(response => (this.info = response))
  }
}
</script>
