/*window.addEventListener('load', (event) => {
  Array.from(document.querySelectorAll('[data-toggle="tooltip"]'))
      .forEach(toastNode => new bootstrap.Tooltip(toastNode))
});*/

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
