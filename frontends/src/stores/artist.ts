import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from 'axios';

import { axiosErrorObject } from './helpers';

export const useArtistDetailStore = defineStore("artistDetail", () => {
  const artist = ref({});
  const error = ref({});

  function init() {
    artist.value = {};
    error.value = {};
  }
  async function load(artist_slug: String) {
    init();
    await axios.get(`http://localhost:8002/api/artists/${artist_slug}/`)
      .then(res => artist.value = res.data)
      .catch(err => error.value = axiosErrorObject(err));
  }

  return { artist, error, load };
});
