import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from 'axios';
import _filter from 'lodash/filter'
import _map from 'lodash/map'

import { axiosApiError, apiUrl } from './helpers';
import type { ArtistCategory, ApiError } from './types';

export const useCategoryListStore = defineStore("categoryList", () => {
  const categories = ref<ArtistCategory[]|undefined>();
  const error = ref<ApiError|undefined>();

  function init() {
    categories.value = undefined;
    error.value = undefined;
  }
  async function load() {
    init();
    await axios.get(apiUrl('/categories/'))
      .then(res => categories.value = _map(res.data, c => ({
        ...c,
        permalink: `/c/${c.slug}/`,
      })) as [ArtistCategory])
      .catch(err => error.value = axiosApiError(err));
  }

  function categoriesRoot(): ArtistCategory[]|[] {
    return _filter(categories.value, {parent: null}) as ArtistCategory[]
  }

  function getCategoryBySlug(slug: string): ArtistCategory|undefined {
    return _filter(categories.value, {slug: slug})[0]
  }

  return { categories, error, load, categoriesRoot, getCategoryBySlug };
});
