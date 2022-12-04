import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from 'axios';

import { axiosApiError, apiUrl } from './helpers';
import type { ArtistCategory, ApiError } from './types';

export const useCategoryListStore = defineStore("categoryList", () => {
  const categories = ref<[ArtistCategory]|undefined>();
  const error = ref<ApiError|undefined>();

  function init() {
    categories.value = undefined;
    error.value = undefined;
  }
  async function load() {
    init();
    await axios.get(apiUrl('/categories/'))
      .then(res => categories.value = res.data as [ArtistCategory])
      .catch(err => error.value = axiosApiError(err));
  }

  return { categories, error, load };
});
