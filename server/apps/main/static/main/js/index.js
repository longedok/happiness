Vue.createApp({
  data() {
    let selectedTopic = {words: []};
    let currentPage = "words-trainer";

    if (topics.length > 0) {
      selectedTopic = topics[0];
      selectedTopic.selected = true;
    }

    return {
      selectedTopic: selectedTopic,
      topics: topics,
      currentPage: currentPage
    }
  },
  methods: {
    selectTopic(topic, event) {
      this.selectedTopic.selected = false;
      this.selectedTopic = topic;
      this.selectedTopic.selected = true;
    },
    changePage(page, event) {
      this.currentPage = page;
    },
    toggleCard(word, event) {
      word.open = !word.open;
    }
  }
}).mount('#app');
