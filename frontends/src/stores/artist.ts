import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from 'axios';
import _filter from 'lodash/filter'
import _uniqBy from 'lodash/uniqBy'

import { axiosApiError, apiUrl } from './helpers';
import type { Artist, ApiError } from './types';

export const useArtistDetailStore = defineStore("artistDetail", () => {
  const artist = ref<Artist|undefined>();
  const error = ref<ApiError|undefined>();

  function init() {
    artist.value = undefined;
    error.value = undefined;
  }
  function set(data: any) {
    artist.value = {
      ...data,
      birth_date: data.birth_date ? new Date(data.birth_date) : null
    } as Artist
  }
  function fail(err: any) {
    artist.value = undefined
    error.value = axiosApiError(err)
  }
  async function load(artist_slug: String) {
    init();
    await axios.get(apiUrl(`/artists/${artist_slug}/`))
      .then(res => set(res.data))
      .catch(err => fail(err));
  }

  return { artist, error, load };
});

export const useArtistsListStore = defineStore("artistsList", () => {
  const artists = ref<Artist[]|undefined>();
  const error = ref<ApiError|undefined>();

  function init() {
    artists.value = undefined;
    error.value = undefined;
  }
  async function load(category_slug: String|null = null) {
    init();
    let url = apiUrl('/artists/')
    if (category_slug) {
      url = url + `?category=${category_slug}`
    }
    await axios.get(url)
      .then(res => artists.value = res.data as [Artist])
      .catch(err => error.value = axiosApiError(err));
  }

  function artistsByCategory(category_slug: String): Artist[] {
    return _uniqBy(Array().concat(
      _filter(artists.value, {categories: [{slug: category_slug}]}),
      _filter(artists.value, {categories: [{parent: {slug: category_slug}}]})
    ), 'slug')
  }

  return { artists, error, load, artistsByCategory };
});
