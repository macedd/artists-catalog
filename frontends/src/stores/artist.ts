import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from 'axios';
import _filter from 'lodash/filter'
import _uniqBy from 'lodash/uniqBy'
import _find from 'lodash/find'
import _orderBy from 'lodash/orderBy';

import { axiosApiError, apiUrl } from './helpers';
import { type Artist, type ArtistPortfolioType, type ArtistPortfolio, type ApiError, ReadyStateType } from './types';

export const useArtistDetailStore = defineStore("artistDetail", () => {
  const artist = ref<Artist|undefined>();
  const error = ref<ApiError|undefined>();
  const state = ref<ReadyStateType|undefined>();

  function init() {
    artist.value = undefined;
    error.value = undefined;
    state.value = undefined;
  }
  function success(data: any) {
    artist.value = {
      ...data,
      birth_date: data.birth_date ? new Date(data.birth_date) : null,
      permalink: `/a/${data.slug}/`,
    } as Artist
    state.value = ReadyStateType.SUCCESS
  }
  function fail(err: any) {
    artist.value = undefined
    error.value = axiosApiError(err)
    state.value = ReadyStateType.ERROR
  }
  async function load(artist_slug: String) {
    init();
    state.value = ReadyStateType.LOADING
    await axios.get(apiUrl(`/artists/${artist_slug}/`))
      .then(res => success(res.data))
      .catch(err => fail(err));
    }

  return { artist, error, state, load };
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
      .then(res => artists.value = _uniqBy(res.data as Object[], 'slug') as Artist[])
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

export const useArtistHelpers = defineStore("artistHelpers", () => {
  function portfolioByType(artist: Artist, portfolio_type: ArtistPortfolioType): ArtistPortfolio[] {
    return _filter(artist.portfolio, {upload_type: portfolio_type});
  }
  function portfolioById(artist: Artist, portfolio_id: Number): ArtistPortfolio | undefined {
    return _find(artist.portfolio, {id: portfolio_id});
  }
  function rankArtistsByWeightedScore(artists: Artist[]): Artist[] {
    return _orderBy(artists, ['rank'], ['desc']);
  }

  return { portfolioByType, portfolioById, rankArtistsByWeightedScore };
});