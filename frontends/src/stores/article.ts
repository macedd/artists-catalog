import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from 'axios';

import { axiosApiError, apiUrl } from './helpers';
import type { Article, ApiError } from './types';

export const useArticleListStore = defineStore("articleList", () => {
  const articles = ref<[Article]|undefined>();
  const error = ref<ApiError|undefined>();

  function init() {
    articles.value = undefined;
    error.value = undefined;
  }
  async function load() {
    init();
    await axios.get(apiUrl('/articles/'))
      .then(res => articles.value = res.data as [Article])
      .catch(err => error.value = axiosApiError(err));
  }

  return { articles, error, load };
});
