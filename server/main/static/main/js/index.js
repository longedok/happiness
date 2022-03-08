let app = Vue.createApp({
  data() {
    let selectedTopic = {words: []};

    if (topics.length > 0) {
      selectedTopic = topics[0];
      selectedTopic.selected = true;
    }

    return {
      selectedTopic: selectedTopic,
      topics: topics
    }
  },
  methods: {
    selectTopic(topic, event) {
      this.selectedTopic.selected = false;
      this.selectedTopic = topic;
      this.selectedTopic.selected = true;
    },
    setStatus(word, status, event) {
      let method;
      switch (status) {
        case "new":
          method = "set_new";
          break;
        case "learning":
          method = "set_learning";
          break;
        case "learned":
          method = "set_learned";
          break;
        default:
          return;
      };
      fetch(`/api/words/${word.id}/${method}/`, {
        method: "post",
        headers: {
          "x-csrftoken": csrfToken,
          "content-type": "application/json"
        }
      }).then(res => {
        if (res.ok) {
          word.status = status === "new" ? null : status;
        }
      });
    }
  }
});

app.directive('tooltip', {
  created: () => {
    this.removeTooltip = (el) => {
      if (el.tooltip !== undefined) {
        el.tooltip.dispose();
      }
    }

    this.createTooltip = (el) => {
      el.tooltip = new bootstrap.Tooltip(el);
    }
  },
  mounted: (el) => {
    this.createTooltip(el);
  },
  updated: (el) => {
    this.removeTooltip(el);
    this.createTooltip(el);
  },
  beforeUnmount: (el) => {
    this.removeTooltip(el);
  },
});

app.mount("#app");
