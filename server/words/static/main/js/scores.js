let app = Vue.createApp({
  beforeMount() {
    this.scoreboards = scoreboards;
  },
  data() {
    return {
      scoreboards: this.scoreboards,
    }
  },
  methods: {}
});

app.mount("#app");
