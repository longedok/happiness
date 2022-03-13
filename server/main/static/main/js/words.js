let app = Vue.createApp({
  beforeMount() {
    this.topics = topics;
    this.allWords = words;

    this.filter = {
      "status": null,
      "topic":  (topics.length > 0) ? topics[0].id : null,
    };

    this.filterWords();
  },
  data() {
    return {
      topics: this.topics,
      words: this.words,
      filter: this.filter,
      allWords: this.allWords,
      groups: this.groups,
    }
  },
  methods: {
    playFile(word) {
      let player = document.getElementById(`player-${word.id}`);
      if (player !== undefined) {
        player.play()
      }
    },
    setTopicFilter(topicId, event) {
      if (this.filter.topic === topicId) {
        this.filter.topic = null;
      } else {
        this.filter.topic = topicId;
      };

      this.filterWords();
    },
    setStatusFilter(status, event) {
      if (this.filter.status === status) {
        this.filter.status = null;
      } else {
        this.filter.status = status;
      };

      this.filterWords();
    },
    filterWords() {
      this.words = words.filter(
        word => {
          if (this.filter.status != null) {
            if (word.status !== this.filter.status) {
              return false;
            }
          };
          if (this.filter.topic != null) {
            if (word.topic !== this.filter.topic) {
              return false;
            }
          };
          return true;
        }
      );

      let prevDate;
      for (let i = 0; i < this.words.length; i++) {
        if (this.words[i].date != prevDate) {
          prevDate = this.words[i].date;
          this.words.splice(i, 0, {date: this.words[i].date_display, dateRow: true});
        };
      };

//      const groups = [];
//      let currentGroup;
//      let prevDate;
//      for (const word of this.words) {
//        if (word.date != prevDate) {
//          prevDate = word.date;
//          currentGroup = [];
//          groups.push(currentGroup);
//        }
//        currentGroup.push(word);
//      }
//      this.groups = groups;
    },
    setWordStatus(word, status, event) {
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
          word.status = status;
          this.filterWords();
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
