<script setup lang="ts">
import { computed } from 'vue'
import _orderBy from 'lodash/orderBy';

import type { Artist, ArtistCategory } from '../../stores/types';
import { LayoutHelpers } from '../../stores/layout';
import CategoryArtistsList from './CategoryArtistsList.vue';
import { useArtistHelpers } from '../../stores/artist';

const props = defineProps<{
  category: ArtistCategory;
  artists: Artist[];
}>();

const responsiveItemsCount = LayoutHelpers.carouselItemsToShow()

const popularArtists = computed(() => props.artists.slice(0, responsiveItemsCount.value))
const latestArtists = computed(() => _orderBy(props.artists.slice(responsiveItemsCount.value), 'created_at', 'desc'))

const otherArtists = computed(() =>
  useArtistHelpers()
    .rankArtistsByWeightedScore(latestArtists.value.slice(responsiveItemsCount.value)))

</script>

<template>
  <!-- category -->
  <div class="my-4 md:my-8">
    <h1
      class="bg-[#ed702d] py-2 px-8 mt-8 md:mt-8 -mb-2 md:-mb-4 text-xl font-bold uppercase text-white text-center md:text-3xl">
      Categoria: {{ category.title }}
    </h1>

    <h3
      class="bg-[#212121] py-2 px-8 text-xl mb-2 mt-6 uppercase text-white md:text-3xl">
      Mais clicados
    </h3>
    <CategoryArtistsList :artists="popularArtists" />

    <h3
      class="bg-[#212121] py-2 px-8 text-xl mb-2 mt-6 uppercase text-white md:text-3xl"
      v-if="latestArtists.length">
      Adicionados recentemente
    </h3>
    <CategoryArtistsList :artists="latestArtists.slice(0, responsiveItemsCount)" />

    <h3
      class="bg-[#212121] py-2 px-8 text-xl mb-2 mt-6 uppercase text-white md:text-3xl"
      v-if="otherArtists.length">
      Outros destaques
    </h3>
    <CategoryArtistsList :artists="otherArtists" />
</div>
</template>